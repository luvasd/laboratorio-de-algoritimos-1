# inicializa as variáveis de contagem e soma das idades
total_idades_otimo = 0
quantidade_otimo = 0
quantidade_regular = 0
quantidade_bom = 0

# coleta as informações de idade e opinião dos 15 espectadores
for i in range(15):
    idade = int(input(f"Informe a idade do espectador {i+1}: "))
    opiniao = int(input("Informe a opinião do espectador (1-regular, 2-bom, 3-ótimo): "))

    # calcula a média das idades das pessoas que responderam ótimo
    if opiniao == 3:
        total_idades_otimo += idade
        quantidade_otimo += 1

    # conta a quantidade de pessoas que responderam regular, bom e ótimo
    if opiniao == 1:
        quantidade_regular += 1
    elif opiniao == 2:
        quantidade_bom += 1

# calcula a média das idades das pessoas que responderam ótimo
if quantidade_otimo > 0:
    idade_media_otimo = total_idades_otimo / quantidade_otimo
else:
    idade_media_otimo = 0

# calcula a porcentagem de pessoas que responderam bom entre todos os espectadores analisados
porcentagem_bom = (quantidade_bom / 15) * 100

# exibe a média das idades das pessoas que responderam ótimo, a quantidade de pessoas que responderam regular e a porcentagem de pessoas que responderam bom
print(f"Média das idades das pessoas que responderam ótimo: {idade_media_otimo:.2f}")
print(f"Quantidade de pessoas que responderam regular: {quantidade_regular}")
print(f"Porcentagem de pessoas que responderam bom: {porcentagem_bom:.2f}%")
