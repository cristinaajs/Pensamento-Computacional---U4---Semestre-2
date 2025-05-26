lado1 = float(input("Digite um dos lados: "))
lado2 = float(input("Digite outro lado: "))
lado3 = float(input("Digite um último lado: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if lado1 == lado2 == lado3:
        print ("triângulo Equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print ("triângulo Isóceles")
    else:
        print ("triângulo Escaleno")
else:
    print("Inválido")