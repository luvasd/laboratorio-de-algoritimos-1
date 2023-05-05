# inicializa as variáveis de contagem e soma das idades
total_idades = 0
total_idades_mulheres = 0
total_idades_homens = 0
quantidade_mulheres = 0
quantidade_homens = 0

# coleta as informações de idade e sexo das sete pessoas
for i in range(7):
    idade = int(input(f"Informe a idade da pessoa {i+1}: "))
    sexo = input(f"Informe o sexo da pessoa {i+1} (M/F): ")

    # incrementa o contador de idades e o contador correspondente ao sexo da pessoa atual
    total_idades += idade
    if sexo == 'F':
        total_idades_mulheres += idade
        quantidade_mulheres += 1
    elif sexo == 'M':
        total_idades_homens += idade
        quantidade_homens += 1

# calcula as idades médias do grupo, das mulheres e dos homens
idade_media_grupo = total_idades / 7
if quantidade_mulheres > 0:
    idade_media_mulheres = total_idades_mulheres / quantidade_mulheres
else:
    idade_media_mulheres = 0
if quantidade_homens > 0:
    idade_media_homens = total_idades_homens / quantidade_homens
else:
    idade_media_homens = 0

# exibe as idades médias do grupo, das mulheres e dos homens
print(f"Idade média do grupo: {idade_media_grupo:.2f}")
print(f"Idade média das mulheres: {idade_media_mulheres:.2f}")
print(f"Idade média dos homens: {idade_media_homens:.2f}")
