valorDeCombustivel = float(input("Digite o valor do combustivel:" ))

distribuicao = valorDeCombustivel * 0.17

etanol = valorDeCombustivel * 0.12

icms = valorDeCombustivel * 0.28

cide = valorDeCombustivel * 0.07

valorRefinado = distribuicao + etanol + icms + cide

valorFinal = valorDeCombustivel - valorRefinado

print("O valor de refinaria é:", valorFinal)
