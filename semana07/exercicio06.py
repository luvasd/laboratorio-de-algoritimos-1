def menu():
    print("1-sacar")
    print("2-depositar")
    print("3-saldo")
    print("4-sair")
    opcao = int(input("opção:" ))
    return opcao

def sacar(saldo):
    retirada = float(input("QUANTO dejesa retirar: "))
    if saldo >= retirada:
        saldo -= retirada
        print("seu novo saldao: ", saldo)
    else:
        print("saldo insuficiente")
    return saldo

def depositar(saldo):
    deposito = float(input("deposite? " ))
    if deposito < 0:
        print("Não é possivel")
    return deposito
    
def mostarSaldo(saldo):
    print("seu saldo é: ", saldo)


def main():
    saldo = 1000
    opc = 0
    
    while opc != 4:
        opc = menu()
        print("opção digitado:", opc)
        if opc == 1:
            saldo = sacar(saldo)
        elif opc == 2:
            saldo += depositar(saldo)
        elif opc == 3:
            mostarSaldo(saldo)
        elif opc == 4:
            print("Até mais, Bom dia seu pobre.")

        
main()
