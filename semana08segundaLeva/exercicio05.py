def somaNumNaturais(numero):
    soma = 0
    for i in range(1, numero + 1):
        soma += i
    return soma

def main():
    resultado = somaNumNaturais(5)
    print(resultado)  

main()
