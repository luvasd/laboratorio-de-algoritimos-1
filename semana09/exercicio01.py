def lerValores(vetor):
    for valorr in range(10):
        valorr = int(input("Digite valores distintos: " ))
        vetor.append(valorr)
    return vetor
        

def mostrarValores(vetor):
    for i in vetor:
        # i = vetor[0]
        # i = vetor[1]
        print(i)



def main():
    vetor = []
    vetor = lerValores(vetor)
    mostrarValores(vetor)

main()
