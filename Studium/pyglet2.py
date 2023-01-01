import pyglet
from math import sin, cos

window = pyglet.window.Window()
y = 0

def tik(t):
    quaxly.x = quaxly.x + t*20
    quaxly.y = quaxly.y + 10*sin(quaxly.y+t)
    quaxly.rotation = quaxly.rotation+t*10

def zmen(t):
    quaxly.image = obrazek2

pyglet.clock.schedule_interval(tik, 1/30)
pyglet.clock.schedule_once(zmen, 5)

def zpracuj_text(text):
    quaxly.x = 150
    quaxly.y = 0
    quaxly.rotation = 0

obrazek = pyglet.image.load('quaxly.png')
quaxly = pyglet.sprite.Sprite(obrazek)
obrazek2 = pyglet.image.load('quaxly2.png')



def vykresli():
    window.clear()
    quaxly.draw()

def klik(x, y, tlacitko, mod):
    quaxly.x=x
    quaxly.y=y

window.push_handlers(on_text=zpracuj_text, on_draw=vykresli, on_mouse_press=klik)

pyglet.app.run()