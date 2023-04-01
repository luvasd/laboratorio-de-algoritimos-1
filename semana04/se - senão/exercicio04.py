n1 = int(input("Digite um valor para calcular: "))

n2 = int(input("Digite outro valor para calcular: "))

print("1 - Somar os dois")
print("2 - subtração os dois valores")
print("3 - multiplicar os dois valores")
print("4 - dividir os dois valores")
opcao = int(input("Digite uma opção de calcula: "))

if opcao == 1:
    soma = n1 + n2
    print("A soma é: ", soma)
elif opcao == 2:
    sub = n1 - n2
    print("A subtração é: ", sub)
elif opcao == 3:
    mult = n1 * n2
    print("A multiplicação é: ", mult)
elif opcao == 4:
    dividi = n1 / n2
    print("A divisão é: ", dividi)
