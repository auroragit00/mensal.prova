class Produto:
    def __init__(self, descricao, preco_unitario, estoque):
        self.descricao = descricao
        self.preco_unitario = preco_unitario
        self.estoque = estoque

    def decrementar_estoque(self, quant):
        if quant <= 0:
            return False

        if quant > self.estoque:
            return False

        self.estoque -= quant
        return True