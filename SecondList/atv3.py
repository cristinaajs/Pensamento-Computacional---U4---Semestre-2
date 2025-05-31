# Carregar imagem imagem = Image.open("exemplo.jpg") 
 
from PIL import Image
import os

imagem_nome = r"D:\Programação\Computação UEL\Pensamento Computacional - U4 - Semestre 2\think.jpg"

if os.path.exists(imagem_nome):
    imagem = Image.open(imagem_nome)
    
    nova_imagem = imagem.convert("L")
    nova_imagem.save("preto_branco_atv3.jpg")
    print("Imagem convertida para preto e branco salva como 'preto_branco.jpg'.")  
    print("A imagem está em preto e branco")
else:
    print("Arquivo não encontrado. Verifique e tente mais uma vez")