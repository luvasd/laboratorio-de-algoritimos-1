def lerMetros():
    #metros = float(input("Digite quantos metros quer converter: " ))
    return float(input("Digite quantos metros quer converter: " ))

def decimetro(metros):
    return metros * 10

def centimetros(metros):
    return metros * 100

def milimetros(metros):
    return metros * 1000

def main():
    metros = lerMetros()
    decimetros = decimetro(metros)
    centimetross = centimetros(metros)
    milimetross = milimetros(metros)
    print(decimetros, "decimetros")
    print(centimetross, "centímetros")
    print(milimetross, "milimetros")


main()
