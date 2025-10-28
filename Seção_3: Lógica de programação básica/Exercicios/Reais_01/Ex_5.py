#Problema 5: Sistema de Carrinho de Compras

class CarrinhoCompras:
    def __init__(self):
        self.itens = []
        self.desconto = 0
    
    def adicionar_item(self, nome, preco, quantidade=1):
        """Adiciona um item ao carrinho"""
        pass
    
    def remover_item(self, nome):
        """Remove um item do carrinho"""
        pass
    
    def calcular_total(self):
        """Calcula o total considerando quantidade e desconto"""
        pass
    
    def aplicar_desconto(self, percentual):
        """Aplica um desconto percentual"""
        pass
    
    def finalizar_compra(self):
        """Finaliza a compra e retorna resumo"""
        pass

# Teste rápido:
carrinho = CarrinhoCompras()
carrinho.adicionar_item("Notebook", 2500.00)
carrinho.adicionar_item("Mouse", 50.00, 2)