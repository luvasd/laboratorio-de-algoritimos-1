def menu():
    print("1 - Inserir item")
    print("2 - Retirer item")
    print("3 - Listar itens")
    print("4 - Sair")
    opc = int(input("Digite sua opção: "))
    return opc

def inserirItem(vetor):
    item = int(input("Digite um item para adicionar a lista: " ))
    vetor.append(item)
    return vetor

def retirarItem(vetor):
    retiraItem = int(input("Digite um item para retirar da lista: " ))
    vetor.remove(retiraItem)
    return vetor

def mostrarlista(vetor):
    print(vetor)


def main():
    opc = 0
    vetor = []
    while opc != 4:
        opc = menu()
        if opc == 1:
            adcAlista = inserirItem(vetor)
        elif opc == 2:
            retira = retirarItem(vetor)
        elif opc == 3:
            mostrar = mostrarlista(vetor)
        elif opc == 4:
            print("Até a proxima")
        else:
            print("opção invalida")

main()

