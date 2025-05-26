idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
    print("Categoria: Criança")
elif idade >= 13 and idade <= 17:
    print("Categoria: Adolescente")
elif idade >= 18:
    print("Categoria: Adulto")
else:
    print("Inválido")