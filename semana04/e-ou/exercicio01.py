nome = input("Digite o nome do funcionario: ")

tempoTrampo = int(input("Digite quantos anos de serviço o funcionario tem: "))

salario = float(input("Digite o salario do funcionario: "))

if tempoTrampo >= 5 and salario <= 2000:
    print("O funcionario", nome, "tem direito a ganhar aumento de 10%")
else:
    print("O funcionario", nome, "tem direito a ganhar aumento de 5%")

