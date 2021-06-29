#Equipo 7
# Irina Kaminsky Castillo
# Axel Gael Uzeta Gomez
# Edgar Zúñiga Sánchez

from turtle import *

from freegames import vector
import turtle


# def line(start, end):
#     "Draw line from start to end."
#     up()
#     goto(start.x, start.y)
#     down()
#     goto(end.x, end.y)
# 
# 
# def square(start, end):
#     "Draw square from start to end."
#     up()
#     goto(start.x, start.y)
#     down()
#     begin_fill()
# 
#     for count in range(4):
#         forward(end.x - start.x)
#         left(90)
# 
#     end_fill()
# 
# 
# def circle(start, end):
#     "Draw circle from start to end."
#     pass  # TODO
# 
# 
# def rectangle(start, end):
#     "Draw rectangle from start to end."
#     pass  # TODO
# 
# 
#def triangle(start, end):
#     "Draw triangle from start to end."
#     pass  # TODO
# 
# 
# def tap(x, y):
#     "Store starting point or draw shape."
#     start = state['start']
# 
#     if start is None:
#         state['start'] = vector(x, y)
#     else:
#         shape = state['shape']
#         end = vector(x, y)
#         shape(start, end)
#         state['start'] = None
# 
# 
# def store(key, value):
#     "Store value in state at key."
#     state[key] = value
# 
# 
# state = {'start': None, 'shape': line}
# setup(420, 420, 370, 0)
# onscreenclick(tap)
# listen()
# onkey(undo, 'u')
# onkey(lambda: color('black'), 'K')
# onkey(lambda: color('white'), 'W')
# onkey(lambda: color('green'), 'G')
# onkey(lambda: color('blue'), 'B')
# onkey(lambda: color('red'), 'R')
onkey(lambda: color('orange'), 'O') # Se agrega nuevo color

# onkey(lambda: store('shape', line), 'l')
# onkey(lambda: store('shape', square), 's')
# onkey(lambda: store('shape', circle), 'c')
# onkey(lambda: store('shape', rectangle), 'r')
# onkey(lambda: store('shape', triangle), 't')
# done()


# Dibujar Circulo
t = turtle.Turtle()  
r = 50
t.circle(r)

#Completar un rectangulo 
t = turtle.Turtle()
t.color("white")
t.goto (200,0)
t.color("red")

l = 200
w = 100

# se dibuja primer lado
t.left(90)
t.forward(w) # Hacia adelante una unidad w
 
# se dibuja segundo lado
t.left (-90)
t.forward(l) # Hacia adelante una unidad l
 
# se dibuja tercer lado
t.left(-90)
t.forward(w) # Hacia adelante una unidad w

# se dibuja cuarto lado
t.left(-90)
t.forward(l) # Hacia adelante una unidad l

#Completar el triangulo

board = turtle.Turtle()
t.color("white")
t.goto (200,-100)
t.color("purple")
 
t.forward(100) # se dibuja base
 
t.left(120)
t.forward(100) # se definen angulos
 
t.left(120)
t.forward(100)
 
turtle.done()
