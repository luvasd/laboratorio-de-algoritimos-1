def recebeVetor(vetor):
    t = len(vetor)
    maiorValor = vetor[0]
    posiMaior = 0
    menorValor = vetor[0]
    posiMenor = 0
    maiores100 = 0
    par = 0
    impar = 0
    #print("maior valor: ", maiorValor)
    #print("Menor valor: ", menorValor)
    for i in range(0,t):
        if vetor[i] > maiorValor:
            #print("O ", vetor[i], "na posicao:", i, "eh maior que: ", maiorValor)
            maiorValor = vetor[i]
            posiMaior = i
        elif vetor[i] < menorValor:
            #print("O ", vetor[i], "na posicao:", i, "eh maior que: ", menorValor)
            menorValor = vetor[i]
            posiMenor = i
    print("O maior é: ", maiorValor, "E o menor valor é: ", menorValor)
    for i in range(0,t):
        soma = vetor[0] + vetor[i]
        media = soma / t
    print(media)
    for i in range(0,t):
        if vetor[i] > 100:
            maiores100 += 1
        elif vetor[i] % 2 == 0:
            par += 1
        elif vetor[i] % 2 != 0:
            impar += 1
    print("impar", impar, "par", par)

def main():
    vetor = [1,5,55,111,2022,234,987,78,56,7007]
    recebeVetor(vetor)
main()
