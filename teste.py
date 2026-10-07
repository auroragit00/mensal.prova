from produto import Produto
from venda import Venda


# Criando os produtos
produto1 = Produto("Caderno", 20.00, 10)
produto2 = Produto("Caneta", 3.50, 20)


# Criando uma venda
venda = Venda()


# Adicionando produtos à venda
venda.adicionar_item(produto1, 2)
venda.adicionar_item(produto2, 3)


# Mostrando os resultados
print("===== SISTEMA DE VENDAS =====")

print("\nPRODUTOS:")
print(f"{produto1.descricao} - R$ {produto1.preco_unitario:.2f}")
print(f"Estoque: {produto1.estoque}")

print(f"\n{produto2.descricao} - R$ {produto2.preco_unitario:.2f}")
print(f"Estoque: {produto2.estoque}")


print("\nITENS DA VENDA:")

for item in venda.itens:
    print(
        f"{item.produto.descricao} x {item.quantidade} "
        f"= R$ {item.calcular_subtotal():.2f}"
    )


print(f"\nVALOR TOTAL: R$ {venda.calcular_total():.2f}")

print(
    f"DATA DA VENDA: "
    f"{venda.data.strftime('%d/%m/%Y %H:%M:%S')}"
)


# Testando venda com estoque insuficiente
print("\nTESTE DE ESTOQUE:")

resultado = venda.adicionar_item(produto1, 20)

if resultado:
    print("Venda realizada!")
else:
    print("Venda não realizada: estoque insuficiente.")
    