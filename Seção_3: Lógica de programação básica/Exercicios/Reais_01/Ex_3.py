#Problema 3: Sistema de Gerenciamento de Tarefas

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
    
    def adicionar_tarefa(self, descricao, prioridade="normal"):
        """
        Adiciona uma tarefa com descrição e prioridade
        Prioridades: "baixa", "normal", "alta"
        """
        pass
    
    def concluir_tarefa(self, indice):
        """Marca uma tarefa como concluída"""
        pass
    
    def listar_tarefas_pendentes(self):
        """Retorna lista de tarefas não concluídas"""
        pass
    
    def estatisticas(self):
        """Retorna dicionário com total, concluídas e pendentes"""
        pass

# Teste o sistema:
gt = GerenciadorTarefas()
gt.adicionar_tarefa("Estudar Python", "alta")
gt.adicionar_tarefa("Fazer exercícios", "normal")