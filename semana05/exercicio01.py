somaAltura = 0
somaIdade = 0 
pessoas = 0
opc = 0 
mediaAltura = 0 
mediaIdade = 0

while opc != 3:
    print("1 - Cadastrar pessoa")
    print("2 - Mostrar media parcial")
    print("3 - Sair")
    opc = int(input("Opção:" ))

    if opc == 1:
        altura = float(input("Digite sua altura: " ))
        idade = int(input("Digite sua idade: " ))
        somaAltura += altura
        somaIdade += idade
        pessoas += 1
        mediaAltura = somaAltura / pessoas
        mediaIdade = somaIdade / pessoas 
    elif opc == 2:
        print("media parcial de altura é", mediaAltura)
        print("media parcial da idade é", mediaIdade)
    elif opc == 3:
        print("Sair")
    else:
        print("Opção Invalida")
print("media parcial de altura é", mediaAltura)
print("media parcial da idade é", mediaIdade)

