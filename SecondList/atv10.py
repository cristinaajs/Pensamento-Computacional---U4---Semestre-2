from vpython import *
from math import sin, cos, pi

scene.background = color.white

raio = 5

mostrador = ring(pos=vector(0, 0, 0), axis=vector(0, 0, 1),
                 radius=raio, thickness=0.1, color=color.purple)

for i in range(12):
    ang = 2 * pi * i / 12
    x = raio * 0.9 * cos(ang)
    y = raio * 0.9 * sin(ang)
    box(pos=vector(x, y, 0), size=vector(0.3, 0.6, 0.1), color=color.purple)

hora = 8
minuto = 40

angulo_horas = 2 * pi * ((hora % 12) / 12 + minuto / 720)
angulo_minutos = 2 * pi * (minuto / 60)

ponteiro_horas = arrow(pos=vector(0, 0, 0),
                       axis=vector(2.5 * cos(angulo_horas), 2.5 * sin(angulo_horas), 0),
                       shaftwidth=0.2, color=color.orange)

ponteiro_minutos = arrow(pos=vector(0, 0, 0),
                         axis=vector(4 * cos(angulo_minutos), 4 * sin(angulo_minutos), 0),
                         shaftwidth=0.2, color=color.green)

while True:
    rate(10)
