from vpython import sphere, vector, color, rate, scene
  
scene.background = color.black 
  
sol = sphere(pos=vector(0, 0, 0), radius=2, color=color.yellow) 
  
t = 0 
dt = 0.01 
 
while True: 
    rate(100) 
    t += dt  