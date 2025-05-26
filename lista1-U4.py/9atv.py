valor = float(input("Digite o valor da sua compra: R$ "))

if valor > 100:
    desconto = valor * 0.10
    valor_final = valor - desconto
    print(f"Você recebeu 10% de desconto. O valor final agora é: R$ {valor_final}")
else:
    print(f"Sem desconto. Valor final R$ {valor}")