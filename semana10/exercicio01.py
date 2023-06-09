def inverterLista(lista):

    tamanhoLista = len(lista)
    n = tamanhoLista - 1
    while(n >= 0):
        print(lista[n])
        n -= 1 

def main():
    lista = [1,2,3,4,5,6,7,8,9,10]
    inverterLista(lista)

main()
