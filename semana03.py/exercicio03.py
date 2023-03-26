dataNasceu = int(input("Digite o seu ano de nascimento:" ))

data2 = 2023 - dataNasceu 

deMaior = data2 >= 18 

if deMaior:
    print("Voçe ja pode votar")

else:
    print("Não pode votar, não é de maior")

