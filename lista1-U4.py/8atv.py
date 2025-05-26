peso = float(input("Digite um peso em kg: "))
altura = float(input("Digite sua altura em m: "))

IMC = peso / (altura*altura)
print(f"O IMC é {IMC:.2f}")

if IMC < 18.5:
    print(f"Abaixo do peso - IMC: {IMC:.2f}")
elif 18.5 <= IMC < 24.9:
    print("Peso normal")
elif 25 <= IMC < 29.9:
    print("Sobrepeso")
elif IMC >= 30:
    print("Obesidade")
else:
    print("Inválido")