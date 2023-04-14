morangos = float(input("Digite quantidade de morangos em KG comprou: " ))

macas = float(input("Digite quantidade em KG de maças vc comprou: " ))

quantidadeTotal = morangos + macas

if quantidadeTotal <= 5:
    quantMorango = morangos * 2.50
    quantMacas = macas * 1.80

    valorTotal = quantMacas + quantMorango

    print("Irão ser pagos pelos", morangos, "kg de morangos e pelos", macas, "kg de maças o valor total de: ", valorTotal)

elif quantidadeTotal > 5:
    quantMorango = morangos * 2.20
    quantMacas = macas * 1.50
    valorTotal = quantMacas + quantMorango

    
    if quantidadeTotal >= 8 or valorTotal > 25:
        valorTotal = valorTotal * 0.90
        print("Voce ira ganhar um desconto de 10%")

    print("Irão ser pagos pelos", morangos, "kg de morangos e pelos", macas, "kg de maças o valor total de: R$", valorTotal)
