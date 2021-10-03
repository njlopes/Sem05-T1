def compra(desconto, parcela, reajuste):
    return desconto, parcela, reajuste


compra = float(input())
desc = compra - (compra * 9 / 100)
parcela = compra / 5
aumento = (compra + (compra * 17 / 100)) / 10
print('%.2f'% desc)
print('%.2f'% parcela)
print('%.2f'% aumento)
