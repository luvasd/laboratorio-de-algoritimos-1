def lerIdades_Media():
    pessoas = 0
    somaIdade = 0
    c18 = 0
    idadePessoas = 0
    for pessoas in range(7):
        idade = int(input("Digite sua idade: " ))

        somaIdade += idade

        pessoas += 1

        if idade >= 18:
            c18 += 1
        
        if idade >= 10 and idade <= 30:
            idadePessoas += 1
            
    porcentagemPessoas = (idadePessoas / pessoas) * 100
    mediaIdade = somaIdade / pessoas

    return mediaIdade, porcentagemPessoas, c18

def main():
    mediaIdade, porcentagem, c18 = lerIdades_Media()
    print(mediaIdade)
    print(porcentagem)
    print(c18)

main()
