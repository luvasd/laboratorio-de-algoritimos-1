respostaPosi = 0

p1 = input("Telefonou para a vitima: ").upper()
if p1 == "SIM":
    respostaPosi += 1

p2 = input("Esteve no local: ").upper()
if p2 == "SIM":
    respostaPosi += 1

p3 = input("Mora perto da vitima: ").upper()
if p3 == "SIM":
    respostaPosi += 1
p4 = input("Devia para a vitima: ").upper()
if p4 == "SIM": 
    respostaPosi += 1
p5 = input("Ja trabalhou com a vitima: ").upper()
if p5 == "SIM":
    respostaPosi += 1

if respostaPosi == 5:
    print("Vc é o assassino")
elif respostaPosi == 4 or respostaPosi == 3:
    print("VC é cumplice")
elif respostaPosi == 2:
    print("Vc é suspeito")
else:
    print("VC é inocente ")
