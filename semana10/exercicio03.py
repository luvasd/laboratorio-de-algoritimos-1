def criar_array():
    array = []
    for i in range(5):
        num = int(input("Digite um número inteiro: "))
        array.append(num)
    return array

def encontrar_maior_menor(array):
    maior_numero = array[0]
    menor_numero = array[0]
    posicao_maior = 0
    posicao_menor = 0

    for i in range(1, len(array)):
        if array[i] > maior_numero:
            maior_numero = array[i]
            posicao_maior = i
        if array[i] < menor_numero:
            menor_numero = array[i]
            posicao_menor = i

    return maior_numero, posicao_maior, menor_numero, posicao_menor

def exibir_resultados(maior_numero, posicao_maior, menor_numero, posicao_menor):
    print("Maior número:", maior_numero)
    print("Posição do maior número:", posicao_maior)
    print("Menor número:", menor_numero)
    print("Posição do menor número:", posicao_menor)

def main():
    
    array = criar_array()
    maior, posicao_maior, menor, posicao_menor = encontrar_maior_menor(array)
    exibir_resultados(maior, posicao_maior, menor, posicao_menor)

main()
