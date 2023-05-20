def calcularPorcentagem(usamA, usamB, usamC):
    porcentagemA = (usamA / 10) * 100
    porcentagemB = (usamB / 10) * 100
    porcentagemC = (usamC / 10) * 100
    print("O total de pessoas q usam o elevador A são: ", porcentagemA,"%")
    print("O total de pessoas q usam o elevador B são: ", porcentagemB,"%")
    print("O total de pessoas q usam elevador C são: ", porcentagemC,"%")

def elevador():
    pessoas = 0
    usamA = 0
    usamB = 0
    usamC = 0
    for i in range(10):
        elevadorusado = input("Qual o elevador q vc mais utiliza?(A, B ou C) " ).upper()
        pessoas += 1
        if elevadorusado == "A":
            usamA += 1
        elif elevadorusado == "B":
            usamB += 1
        elif elevadorusado == "C":
            usamC += 1
        else:
            print("Opção invalida, digite uma opção valida")
    calcularPorcentagem(usamA, usamB, usamC)


def main():
    elevador()

main()

