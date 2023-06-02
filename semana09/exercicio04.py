def lerNum(vetor):
    for i in range(5):
        valor = int(input("Digite um numero: " ))
        vetor.append(valor)
    return vetor
def somaNum(vetor):
    soma = 0
    for valor in vetor:
        soma = soma + valor
    return soma
def mediaNum(vetor):
    recebeSoma = somaNum(vetor)
    media = recebeSoma / len(vetor)
    print(media)
    print(recebeSoma)


def main():
    vetor = []
    vetor = lerNum(vetor)
    mediaNum(vetor)
main()
