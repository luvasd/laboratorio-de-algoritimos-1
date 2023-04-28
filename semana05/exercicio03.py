pessoas = 0
somaIdade = 0
mediaIdade = 0
pessoasIdade = 0
idadePessoas = 0

while pessoas < 7:
    idade = int(input("Digite sua idade: "))
    
    somaIdade += idade

    pessoas += 1

    mediaIdade = somaIdade / pessoas

    if idade >= 18:
        pessoasIdade += 1

    if idade > 10 and idade < 30:
        idadePessoas += 1
        porcentagemPessoas = (idadePessoas / pessoas) * 100
print("A media das 7 pessoas é: ",mediaIdade)
print("Pessoas maiores q 18 anos são: ",pessoasIdade)
print("A porcentagem de pessoas entre 10 e 30 anos são: ",porcentagemPessoas)
        
