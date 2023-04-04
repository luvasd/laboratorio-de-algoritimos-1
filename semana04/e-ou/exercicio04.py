nota1 = float(input("Digite a sua primeira nota: "))

nota2 = float(input("Digite a sua segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 9.0 and media == 10.0:
    print("O aluno com nota", nota1, "e", nota2, "Ficou com media de", media)
    print("Ficou com conceito A, e esta Aprovado")

elif media < 9.0 and media >= 7.5:
    print("O aluno com nota", nota1, "e", nota2, "Ficou com media de", media)
    print("Ficou com conceito B, e esta Aprovado")

elif media < 7.5 and media >= 6.0:
    print("O aluno com nota", nota1, "e", nota2, "Ficou com media de", media) 
    print("Ficou com conceito C, e esta Aprovado")

elif media < 6.0 and media >= 4.0:
    print("O aluno com nota", nota1, "e", nota2, "Ficou com media de", media)
    print("Ficou com conceito D, e esta Reprovado")

else: 
    print("O aluno com nota", nota1, "e", nota2, "Ficou com media de", media)
    print("Ficou com conceito E, e esta Reprovado")
