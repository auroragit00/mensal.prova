class ItemVenda:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
        self.valor_item = produto.preco_unitario

    def calcular_subtotal(self):
        return self.valor_item * self.quantidade