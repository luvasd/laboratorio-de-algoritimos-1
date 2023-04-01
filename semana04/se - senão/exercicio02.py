valorRoupa = float(input("Digite o valor da peça de roupa: " ))

print("Opções para se pagar as roupas")
print("1 - À vista")
print("2 - em duas vezes")
print("3 - em três vezes")
opcao = int(input("Digite a sua opção de compra: " ))

if opcao == 1:
    print("vc deve pagar", valorRoupa)
elif opcao == 2:
    valorFinal = valorRoupa / 2
    print("vc deve pagar por cada parcela: ", valorFinal)
else:
    valorFinal = valorRoupa / 3 
    print("vc deve pagar por cada parcela: ", valorFinal)
