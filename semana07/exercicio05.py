def somaImposto(taxaImposto, custo):
    imposto = custo * taxaImposto / 100
    custo += imposto
    return custo


custoItem = 50.0
taxaImposto = 22.0

custoTotal = somaImposto(taxaImposto, custoItem)
print("Custo total com imposto: R$", custoTotal)

