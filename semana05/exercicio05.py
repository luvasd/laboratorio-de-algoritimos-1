soma_salarios = 0
maior_idade = 0
menor_idade = 0
quantidade_mulheres_salario_ate_100 = 0

for i in range(10):
    idade = int(input(f"Informe a idade da pessoa {i+1}: "))
    if i == 0:
        maior_idade = idade
        menor_idade = idade
    else:
        if idade > maior_idade:
            maior_idade = idade
        if idade < menor_idade:
            menor_idade = idade

    sexo = input(f"Informe o sexo da pessoa {i+1} (M/F): ")

    salario = float(input(f"Informe o salário da pessoa {i+1}: "))
    soma_salarios += salario

    if sexo.upper() == "F" and salario <= 100:
        quantidade_mulheres_salario_ate_100 += 1

media_salarios = soma_salarios / 10

print(f"Média de salário do grupo: R${media_salarios:.2f}")
print(f"Maior idade do grupo: {maior_idade} anos")
print(f"Menor idade do grupo: {menor_idade} anos")
print(f"Quantidade de mulheres com salário até R$100,00: {quantidade_mulheres_salario_ate_100}")
