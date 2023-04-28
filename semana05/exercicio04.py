saldo = float(input("Digite o saldo atual:"))

opc = 0
while opc != 4:
    print("1 - Realizar venda")
    print("2 - Retirar dinheiro")
    print("3 - Dinheiro em caixa")
    print("4 - Sair")
    opc = int(input("Opção:"))

    if opc == 1:
        venda = float(input("Valor da venda: "))
        saldo += venda
        print("Saldo atual: ", saldo)
    elif opc == 2:
        retirada = float(input("Valor da retirada: "))
        if retirada <= saldo:
            saldo -= retirada
        else:
            print("Saldo insuficiente!")
    elif opc == 3:
        print("Valor em caixa: ", saldo)
    elif opc == 4:
        print("Até mais!")
    else:
        print("Opção inválida!")
