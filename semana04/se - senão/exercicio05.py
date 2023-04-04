ipoHabilitacao = input("Qual o seu tipo de carteira: ").upper()

if tipoHabilitacao == "A":
    print("pode dirigir apenas motos e triciclos")
elif tipoHabilitacao == "B":
    print("pode dirigir apenas carros de passeio")
elif tipoHabilitacao == "C":
    print("pode dirigir apenas veiculos com carga acima de 3,500 toneladas")
elif tipoHabilitacao == "D":
    print("pode dirigir apenas veiculos com mais de 8 passageiros")
elif tipoHabilitacao == "E":
    print("pode dirigir apenas veiculos com unidade aclopada com mais de 8000 toneladas")
