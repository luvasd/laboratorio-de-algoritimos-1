h = float(input("Digite a sua altura:" ))

sexo = input("Digite o seu sexo:" ).upper()

if sexo == "MASCULINO":
    peso = (72.7 * h) - 58
    print("Seu peso ideal è:", peso)

else:
   peso = (62.1 * h) - 44
   print("Seu peso ideal é:", peso)
   
 
