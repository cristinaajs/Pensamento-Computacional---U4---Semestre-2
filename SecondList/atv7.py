  
from vpython import box, vector, color, rate, scene, keysdown
from math import cos,sin, pi
import random
  
scene.background = color.black 
  
cubo = box(pos=vector(0, 0, 0), size=vector(2,2,2), color=color.purple) 
cubo.rotate(angle=pi/6, axis=vector(0,1,0))
cubo.rotate(angle=pi/6, axis=vector(1,0,0))

cores = [color.red, color.green, color.blue]
cor_atual = 0
  
t = 0 
dt = 0.01 
 
while True: 
    rate(100) 
    t += dt  

    if 'm' in keysdown():
        cor_atual = (cor_atual + 1) % len(cores)
        cubo.color = cores[cor_atual]

        while 'm' in keysdown():
            rate(10)