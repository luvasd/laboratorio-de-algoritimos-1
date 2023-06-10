def horas():
    trabalhadas = [44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44,]
    return trabalhadas


def ausencias():
    hrsausentes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return hrsausentes


def verificarhrs(trabalhadas, hrsausentes): #Opção 1 do menu.
    user = int(input("Qual o seu código do funcionário?: "))
    print("Horas trabalhadas: ", trabalhadas[user])
    print("Horas ausentes: ", hrsausentes[user])


def alterarHrsTrabalhadas(trabalhadas, hrsausentes): #Opção 2 do menu.
    user = int(input("Qual o seu código do funcionário?: "))
    trabalhou = int(input("Quantas horas você trabalhou?: "))
    trabalhadas[user] = trabalhou
    hrsausentes[user] = 44 - trabalhou
    return trabalhadas, hrsausentes


def alterarHrsAusentes(hrsausentes, trabalhadas): #opc 3 do menu.
    user = int(input("Qual o seu código do funcionário?: "))
    faltou = int(input("Quantas horas você esteve ausente?: "))
    hrsausentes[user] = faltou
    trabalhadas[user] = 44 - faltou
    return hrsausentes, trabalhadas


def mostrar_salario(user, trabalhadas): #opc 4 do menu.
    user = int(input("Qual o seu código do funcionário?: "))
    salario = trabalhadas[user] * 50
    print("O seu salário é: ",salario)


def mostrarUsuarios(hrsausentes, hrstrabalhadas): #opc 5 do menu.
    for user in range (0,20):
        print("O usuário ",user, "trabalhou",hrstrabalhadas[user],"e esteve ausente por", hrsausentes[user],"horas.")


def mediaHrsTrabalhadas(hrstrabalhadas): #opc 6 do menu.
    somatrabalhadas = 0
    for user in range(0,20):
        somatrabalhadas+= hrstrabalhadas[user]
    mediatrabalhadas = somatrabalhadas / 20
    print(mediatrabalhadas, "foi a média de horas trabalhadas pelos 20 funcionários.")


def mediaHrsFaltantes(hrsausentes): #opc 7 do menu
    somafaltantes = 0
    for user in range(0,20):
        somafaltantes+= hrsausentes[user]
    mediafaltadas = somafaltantes / 20
    print(mediafaltadas, "foi a média de horas faltadas pelos 20 funcionários.")


def melhorFuncionario(hrstrabalhadas): #opc 8 do menu.
    maishoras = hrstrabalhadas[0]
    codigomelhor = 0
    for user in range(0,20):
        if hrstrabalhadas[user] > maishoras:
            maishoras = hrstrabalhadas[user]
            codigomelhor = user
    print(codigomelhor,"Foi o funcionário com mais horas. Com",maishoras,"horas trabalhadas.")


def piorFuncionario(hrsausentes): #opc 9 do menu.
    menoshoras = hrsausentes[0]
    codigopior = 0
    for user in range(0,20):
        if hrsausentes[user] > menoshoras:
            menoshoras = hrsausentes[user]
            codigopior = user
    print(codigopior,"Foi o funcionário com menos horas. Com",menoshoras,"horas trabalhadas.")


def menu():
    print("1- Verificar o total de horas trabalhadas e ausentes de um funcionário:")
    print("2- Alterar o total de horas trabalhadas de um funcionário:")
    print("3- Alterar o total de horas ausentes de um funcionário:")
    print("4- Mostrar o salário do funcionário:")
    print("5- Mostrar o código do usuário com seu respectivo total de horas:")
    print("6- Média de horas trabalhadas entre todos os funcionários:")
    print("7- Média de horas faltantes entre todos os funcionários:")
    print("8- Código do funcionário com mais horas trabalhadas:")
    print("9- Código do funcionário com mais horas faltantes:")
    print("10- Resetar o vetores:")
    print("11- Sair")




def main():
    trabalhadas = horas()
    hrsausentes = ausencias()
    #hrstrabalhadas, hrsausentes = horas




    while True:
        menu()
        opcao = int(input("Digite o número da opção desejada: "))
        if opcao == 1:
            verificarhrs(trabalhadas, hrsausentes)
        elif opcao == 2:
            alterarHrsTrabalhadas(trabalhadas, hrsausentes)
        elif opcao == 3:
            alterarHrsAusentes(hrsausentes, trabalhadas)
        elif opcao == 4:
            mostrar_salario(trabalhadas)
        elif opcao == 5:
            mostrarUsuarios(hrsausentes, trabalhadas)
        elif opcao == 6:
            mediaHrsTrabalhadas(trabalhadas)
        elif opcao == 7:
            mediaHrsFaltantes(hrsausentes)
        elif opcao == 8:
            melhorFuncionario(trabalhadas)
        elif opcao == 9:
            piorFuncionario(hrsausentes)
        elif opcao == 10:
            trabalhadas = horas()
            hrsausentes = ausencias()
        elif opcao == 11:
            break
        else:
            print("Opção inválida. Digite novamente.")
    print("Programa encerrado.")


main()


