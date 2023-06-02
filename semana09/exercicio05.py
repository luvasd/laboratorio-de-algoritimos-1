def lerNum(vetor):
    for i in range(5):
        valores = int(input("Digite um numero: "))
        vetor.append(valores)
    return vetor

def verificarNum(vetor):
    num = int(input("Digite um numero e veremos se ele esta na lista: "))
    contador = 0
    for i in vetor:
        if num == i:
            contador += 1
    if contador > 0:
        print("Ele esta dentro do vetor.")
    else:
        print("Não esta no vetor")


def main():
    vetor = []
    vetor = lerNum(vetor)
    verificarNum(vetor)

main()
