def lerValores(vetor):
    for valorr in range(10):
        valorr = int(input("Digite valores distintos: " ))
        vetor.append(valorr)
    return vetor
        

def mostrarValores(vetor):
    valor100 = 0
    for valor in vetor:
        if valor >= 100:
            valor100 +=1
    print(valor100)

def main():
    vetor = []
    vetor = lerValores(vetor)
    mostrarValores(vetor)

main()
