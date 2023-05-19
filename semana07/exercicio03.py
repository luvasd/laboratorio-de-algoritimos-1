def aprovado(media):
    if media >= 7:
        print("Aprovado")
def reprovado(media):
    if media < 4:
        print("Reprovado")
def recuperacao(media):
    if media >= 4 and media < 7:
        print("Recuperação")

def main():
    n1 = float(input("Digite a nota do aluno: "))
    n2 = float(input("Digite a segunda nota do aluno: "))
    n3 = float(input("Digite a terceira nota do aluno: "))
    n4 = float(input("Digite a quarta nota do aluno: "))
    n5 = float(input("Digite a quinta nota do aluno: "))

    media = (n1 + n2 + n3 + n4 + n5) / 5

    aprovado(media)
    reprovado(media)
    recuperacao(media)

main()
    
