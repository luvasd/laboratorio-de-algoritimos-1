tipoHabilitacao = input("Qual o seu tipo de carteira: ").upper()

if tipoHabilitacao == "A":
    a = "Motos e triciclos"
    print("pode dirigir apenas", a)
elif tipoHabilitacao == "B":
    b = "carros de passeios"
    print("pode dirigir apenas", b)
elif tipoHabilitacao == "C":
    c = "veículos de carga acima de 3.500 toneladas"
    print("pode dirigir apenas", c)
elif tipoHabilitacao == "D":
    d = "veículos com mais de 8 passageiros"
    print("pode dirigir apenas", d)
elif tipoHabilitacao == "E":
    e = "veículos com unidade aclopada acima de 6.000 toneladas"
    print("pode dirigir apenas", e)
