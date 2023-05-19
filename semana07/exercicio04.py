def laranjas():
    laranjaCompradas = int(input("Quantas laranjas vc comprou: "))
    if laranjaCompradas <= 12:
        valorFinal = laranjaCompradas * 0.40
    elif laranjaCompradas > 12:
        valorFinal = laranjaCompradas * 0.25
    print(valorFinal)



def main():
    laranjas()

main()
    
