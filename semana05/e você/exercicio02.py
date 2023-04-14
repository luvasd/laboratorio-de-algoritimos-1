print("Informe os 3 lados de um triangulo")

a = int(input("Digite o tamanho do lado A do triangoulo: "))

b = int(input("Digite o tamanho do lado B do triangulo: "))

c = int(input("Digite o tamanho o lado C do triangulo: "))

if a + b > c and a + c > b and b + c > a:
        
        if a == b and a == c and b == c:

            print("Esse é um tringulo equilátero")

        elif a == b or a == c or c == b:

            print("Esse é um triangulo Isóceles")

        elif a != b and a != c and c != b:

            print("Esse triangulo é escaleno")

else:
    print("Não é um triangulo") 

