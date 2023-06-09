def lerNum(lista):
    for i in range(5):
        lerNumero = int(input("Digite um numero inteiro : "))
        lista.append(lerNumero)
    return lista
def somaNum(lista):
    lista = lerNum(lista)
    soma = 0
    n = 0
    while n < 5:
        soma += lista[n]
        n += 1
    print(soma)
    return soma

def media(lista):
    resultadoSoma = somaNum(lista)
    mediaa = resultadoSoma / 5
    print(mediaa) 




def main():
    lista = []
    media(lista)

main()
