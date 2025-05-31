from PIL import Image, ImageDraw, ImageFont 
import os
print("Diretório atual:", os.getcwd())

caminho_imagem_atv4 = r"D:\Programação\Computação UEL\Pensamento Computacional - U4 - Semestre 2\think.jpg"

if not os.path.exists(caminho_imagem_atv4):
    print(f"Arquivo {caminho_imagem_atv4} não encontrado.")
else:
 
    # Carregar a imagem 
    imagem = Image.open(caminho_imagem_atv4)  
    
    # Criar um objeto de desenho 
    desenho = ImageDraw.Draw(imagem) 
    
    # Definir a fonte e o tamanho da marca d'água 
    fonte = ImageFont.truetype("arial.ttf", size=40) 
    texto = "Hoje é um bom dia para \nalcançar novas percepções"
    bbox = desenho.textbbox((0, 0), texto, font=fonte)
    largura_texto = bbox[2] - bbox[0]
    altura_texto = bbox[3] - bbox[1] 
    
    # Determinar posição no canto inferior direito 
    largura, altura = imagem.size 
    text_x = (largura - largura_texto) // 2 # Ajuste para alinhar corretamente 
    text_y = (altura - altura_texto) // 2 
    
    # Adicionar a marca d'água 
    desenho.text((text_x, text_y), texto, font=fonte, fill="yellow")
    
    # Salvar a imagem resultante 
    imagem.save("miniatura_marca_atv4.jpg") 
    print("Imagem salva como 'miniatura_marca_atv4.jpg'.") 
    print(f"A nova imagem tem tamanho: {imagem.size}")