# Carregar imagem imagem = Image.open("exemplo.jpg") 
 
from PIL import Image
import os

imagem_nome = r"D:\Programação\Computação UEL\Pensamento Computacional - U4 - Semestre 2\think.jpg"

if os.path.exists(imagem_nome):
    imagem = Image.open(imagem_nome)
 
    angulo = int(input("Digite o ângulo de rotação para a imagem: ")) 
    espelhar = input("Você que espelhar a imagem? (sim/não)")
 
    nova_imagem_atv5 = imagem.rotate(angulo, expand=True)
     

    if espelhar == "sim":
        nova_imagem_atv5 = nova_imagem_atv5.transpose(Image.FLIP_LEFT_RIGHT)

    nova_imagem_atv5.save("rotacionada_atv5.jpg")
    print(f"Imagem convertida para {angulo} escolhido.")
 
else:
    print("Arquivo não encontrado. Verifique e tente novamente")