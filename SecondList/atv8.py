  
from vpython import sphere, vector, color, rate, scene, keysdown
import random
  
scene.background = color.black 
  
circulo1 = sphere(pos=vector(-5, 0, 0), radius=1, color=color.orange)
circulo2 = sphere(pos=vector(5, 0, 0), radius=2, color=color.purple) 

cores = [color.red, color.green, color.blue, color.yellow]
cor_atual = 0
cselec = False
 
while True: 
    rate(100) 

    if 'c' in keysdown():
        if not cselect:
            cor_atual = (cor_atual + 1) % len(cores)
            circulo1.color = cores[cor_atual]
            cselect = True
    else:
        cselect = False