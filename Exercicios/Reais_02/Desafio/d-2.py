from typing import Optional, Dict, Any, List
import datetime
from sqlalchemy import MetaData, select

def _row_to_dict(row) -> Dict[str, Any]: # a entrada é uma row
    """Converte uma row do SQLAlchemy para dict (datas -> ISO)."""
    out: Dict[str, Any] = {} # cria um dicionaria vazio
    for k, v in zip(row.keys(), row): # percorre os pares (nome_caluno, valor)
        if isinstance(v, (datetime.datetime, datetime.date)): 
            # Se o valor for datetime.date converte para string ISO
            out[k] = v.isoformat()
        else: # Caso contraio copia o valor tal como está
            out[k] = v
    return out
# Carrega os metadados das tabelas rotinas_programas e permisoes_usuario
def fetch_rotinas_programadas(engine, nome_usuario: Optional[str] = None) -> Dict[str, Any]:
    meta = MetaData() 
    meta.reflect(bind=engine, only=["rotinas_programadas", "permissoes_usuario"])

    if "rotinas_programadas" not in meta.tables:
        raise RuntimeError("Tabela 'rotinas_programadas' não encontrada")
    
    rot_tbl = meta.tables["rotinas_programadas"]
    perm_tbl = meta.tables.get("permissoes_usuario")

    permitted_ids = None
    perm_obj = None

