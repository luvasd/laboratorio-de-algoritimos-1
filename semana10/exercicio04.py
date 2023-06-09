def lista1():
    vetor1 = []
    for i in range(5):
        num = int(input("Digite um numero para a lista: "))
        vetor1.append(num)
    return vetor1

def lista2():
    vetor2 = []
    for i in range(5):
        num = int(input("Digire um numero para a segunda lista: "))
        vetor2.append(num)
    return vetor2

def somarListas(lista1,lista2):
    soma = []
    for i in range(len(lista1)):
        soma.append(lista1[i] + lista2[i])

    print(soma)

def main():
    
    recebelista1 = lista1()
    recebeLista2 = lista2()
    soma = somarListas(recebelista1,recebeLista2)

main()
