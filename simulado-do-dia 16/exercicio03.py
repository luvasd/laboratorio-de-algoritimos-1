def digiteSaldo():
    seuSaldo = -1
    while seuSaldo < 0:
        seuSaldo = float(input("Digite seu saldo: " ))
    return seuSaldo

def menu():
    print("1 - Sacar")
    print("2 - Depositor")
    print("3 - Apresentar o extrato")
    print("4 - Sair")
    opc = int(input("Digite a sua Opc: " ))
    return opc

def sacar(saldo,vetor):
    quantoQerSacar = float(input("Digite quando vc deseja sacar: " ))
    if quantoQerSacar > saldo:
        while quantoQerSacar > saldo:
            quantoQerSacar = float(input("Digite quando vc deseja sacar: " ))
    saldo = saldo - quantoQerSacar
    vetor.append(-quantoQerSacar)
    print(quantoQerSacar)
    return saldo, vetor

def depositar(saldo,vetor):
    deposit = float(input("Qaunto deseja depositar: " ))
    depositando = deposit + saldo
    vetor.append(deposit)
    print(depositando)
    return depositando,vetor

    
def main():
    vetor = []
    saldo = digiteSaldo()
    opc = 0

    while opc != 4:
        opc = menu()
        if opc == 1:
            saldo,vetor = sacar(saldo,vetor)
        elif opc == 2:
            saldo,vetor = depositar(saldo,vetor)
        elif opc == 3:
            print(vetor)
        elif opc == 4:
            print(saldo)
            print("Obrigado seu pobre")
            break
main()
        
