nota1 = float(input("Digite a sua primeira nota: "))

nota2 = float(input("Digite a sua segunda nota: "))

frequencia = float(input("Digite a sua frequência/presença: "))

mediaNota = (nota1 + nota2) / 2 

if mediaNota >= 7.0 and frequencia >= 75:
    print("Vc esta Aprovado")
elif mediaNota >= 4.0 and mediaNota < 7.0 and frequencia > 75:
    print("Vc entá em Exame")
elif mediaNota < 4.0 or frequencia <= 75:
    print("Vc entá Reprovado")
