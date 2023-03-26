horasTrabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês:" ))

recebePorHora = 35

salario = recebePorHora * horasTrabalhadas

if salario < 1000:
    salarioFinal = salario + 300
    print("Seu salario final é de", salarioFinal)

else:
    print("Seu salario final é de:", salario) 
