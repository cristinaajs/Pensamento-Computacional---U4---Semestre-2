  
from vpython import *
  
scene.background = color.black 
  
cilindro = cylinder(pos=vector(0, 0, 0), axis=vector(0, 5, 0), radius=2, color=color.green) 

cores = [color.purple, color.blue, color.orange, color.yellow]
cor_atual = 0

while True:
    evento = scene.waitfor('click') 
    if evento.pick == cilindro:  
        cor_atual = (cor_atual + 1) % len(cores)
        cilindro.color = cores[cor_atual]
