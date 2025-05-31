from PIL import Image, ImageDraw, ImageFont 
import os
print("Imagem Local:", os.getcwd())

caminho_imagem = "fiat500.jpg"

if not os.path.exists(caminho_imagem):
    print(f"Arquivo {caminho_imagem} não encontrado.")
else:
    # Carregar a imagem  
    imagem = Image.open(caminho_imagem)

    #Exibir imagem
    imagem.show()  
    print("Imagem exibida")