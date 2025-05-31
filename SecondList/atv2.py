# Carregar imagem imagem = Image.open("exemplo.jpg") 
 
from PIL import Image
import os

imagem_nome = r"D:\Programação\Computação UEL\Pensamento Computacional - U4 - Semestre 2\think.jpg"

if os.path.exists(imagem_nome):
    imagem = Image.open(imagem_nome)

    print("Digite os valores desejados para redimensionar a figura: ") 
    largura = int(input("Digite o número da largura: "))
    altura = int(input("Digite o número da altura: "))

    nova_imagem = imagem.resize((largura, altura))
    nova_imagem.save("redimensionada.jpg")

    print("Imagem redimensionada salva como 'redimensionada.jpg'.") 
else:
    print("Arquivo não encontrado. Verifique e tente novamente")