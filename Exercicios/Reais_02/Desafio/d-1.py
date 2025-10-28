import os
import csv
import zipfile
import tempfile
import datetime
import requests
from sqlalchemy import create_engine, MetaData, select
from sqlalchemy.exc import SQLAlchemyError

# Config via env vars (ou crie um .env e exporte antes de executar)
DATABASE_URL = os.environ.get("DATABASE_URL")  # ex: postgresql://user:pass@host:5432/dbname
BACKUP_API_URL = os.environ.get("BACKUP_API_URL", "https://upload.backup.exemple/v1/api/new/backup")
BACKUP_TOKEN = os.environ.get("BACKUP_TOKEN")  # Bearer token
HOST_HEADER = os.environ.get("BACKUP_HOST_HEADER", "upload.backup.exemple")
EXCLUDE_TABLES_RAW = os.environ.get("EXCLUDE_TABLES", "registro tecnicos")  # csv, case-insensitive

# Normalize exclude table names -> set with underscores and spaces removed and lowercase
_EXCLUDE = {
    t.strip().lower().replace(" ", "_")
    for t in EXCLUDE_TABLES_RAW.split(",")
    if t.strip()
}


def table_excluded(table_name: str) -> bool:
    name_norm = table_name.lower().replace(" ", "_")
    return name_norm in _EXCLUDE


def dump_db_except_excluded(database_url: str, tmpdir: str) -> list:
    """
    Faz dump de todas as tabelas (CSV) exceto as excluídas.
    Retorna lista de caminhos dos arquivos CSV gerados.
    """
    engine = create_engine(database_url)
    meta = MetaData()
    meta.reflect(bind=engine)
    csv_paths = []

    with engine.connect() as conn:
        for t_name, table in meta.tables.items():
            if table_excluded(t_name):
                print(f"Pulando tabela excluída: {t_name}")
                continue

            out_path = os.path.join(tmpdir, f"{t_name}.csv")
            print(f"Exportando tabela {t_name} -> {out_path}")
            try:
                sel = select(table)
                result = conn.execute(sel)
                cols = result.keys()

                with open(out_path, "w", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(cols)
                    for row in result:
                        writer.writerow([None if v is None else str(v) for v in row])
                csv_paths.append(out_path)
            except SQLAlchemyError as e:
                print(f"Erro exportando {t_name}: {e}")

    return csv_paths


def make_zip(files: list, dest_path: str):
    with zipfile.ZipFile(dest_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for f in files:
            arcname = os.path.basename(f)
            z.write(f, arcname=arcname)
    print(f"Arquivo zip criado: {dest_path}")


def send_backup(zip_path: str) -> requests.Response:
    headers = {
        "Authorization": f"Bearer {BACKUP_TOKEN}" if BACKUP_TOKEN else "",
        "Host": HOST_HEADER,
    }
    with open(zip_path, "rb") as fh:
        files = {"file": ("backup.zip", fh, "application/zip")}
        resp = requests.put(BACKUP_API_URL, headers=headers, files=files, timeout=300)
    return resp


def main():
    if not DATABASE_URL:
        print("ERRO: DATABASE_URL não definido.")
        return

    now = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    with tempfile.TemporaryDirectory() as tmp:
        csv_files = dump_db_except_excluded(DATABASE_URL, tmp)
        if not csv_files:
            print("Nenhuma tabela exportada (possível erro ou todas excluídas). Abortando.")
            return

        zip_path = os.path.join(tmp, f"backup_{now}.zip")
        make_zip(csv_files, zip_path)

        print("Enviando backup para o endpoint...")
        try:
            resp = send_backup(zip_path)
            if resp.ok:
                print("Backup enviado com sucesso. Código:", resp.status_code)
            else:
                print("Falha no envio. Código:", resp.status_code, "Resposta:", resp.text)
        except requests.RequestException as e:
            print("Erro durante envio:", e)


if __name__ == "__main__":
    main()