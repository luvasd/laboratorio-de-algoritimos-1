def main():

    respostaPessoas = ""

    qtdA = 0

    qtdB = 0

    qtdC = 0

    for pessoas in range(20):

        respostaPessoas = input("Qual o melhor jornal na sua apnião? A,B ou C?" ).upper()

        if respostaPessoas == "A":
            qtdA += 1

        elif respostaPessoas == "B":
            qtdB += 1

        elif respostaPessoas == "C":
            qtdC += 1

    porcentagemA = (qtdA / 20) * 100
    porcentagemB = (qtdB / 20) * 100
    porcentagemC = (qtdC / 20) * 100

    if porcentagemA < porcentagemB and porcentagemA < porcentagemC and porcentagemB < porcentagemC:
        print("O jornal A teve", porcentagemA,"%","o jornal B teve",porcentagemB,"%","e o jornal C teve", porcentagemC,"%")

    elif porcentagemA < porcentagemC and porcentagemA < porcentagemB and porcentagemC < porcentagemB:
        print("O jornal A teve", porcentagemA,"%","o jornal C teve",porcentagemC,"%","e o jornal B teve", porcentagemB,"%")

    elif porcentagemB < porcentagemA and porcentagemB < porcentagemC and porcentagemA < porcentagemC:
        print("O jornal B teve", porcentagemB,"%","o jornal A teve",porcentagemA,"%","e o jornal C teve", porcentagemC,"%")

    elif porcentagemB < porcentagemC and porcentagemB < porcentagemA and porcentagemC < porcentagemA:
        print("O jornal B teve", porcentagemB,"%","o jornal C teve",porcentagemC,"%","e o jornal A teve", porcentagemA,"%")

    elif porcentagemC < porcentagemA and porcentagemC < porcentagemB and porcentagemA < porcentagemB:
        print("O jornal C teve", porcentagemC,"%","o jornal A teve",porcentagemA,"%","e o jornal B teve", porcentagemB,"%")

    elif porcentagemC < porcentagemB and porcentagemC < porcentagemA and porcentagemB < porcentagemA:
        print("O jornal C teve", porcentagemC,"%","o jornal B teve",porcentagemB,"%","e o jornal A teve", porcentagemA,"%")

main() 
