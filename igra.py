# PROJEKT INFORMATIKA - TIJAN NARTNIK, 1. B
# CLOVEK NE JEZI SE

from turtle import *

# pohitrimo turtle
speed(60)

class Polje:
  def __init__(self, barva, x, y):
    self.barva = barva
    self.x = x
    self.y = y

## vsa igralna polja
polja = [
    ## rdeca baza
    Polje("red", -500, -500),
    Polje("red", -450, -500),
    Polje("red", -500, -450),
    Polje("red", -450, -450),

    ## modra baza
    Polje("blue", 500, 500),
    Polje("blue", 450, 500),
    Polje("blue", 500, 450),
    Polje("blue", 450, 450),

    ## zelena baza
    Polje("green", -500, 500),
    Polje("green", -450, 500),
    Polje("green", -500, 450),
    Polje("green", -450, 450),

    ## rumena baza
    Polje("yellow", 500, -500),
    Polje("yellow", 450, -500),
    Polje("yellow", 500, -450),
    Polje("yellow", 450, -450),
]  

def narisiPolje(barva, x, y):
    up()
    goto(x, y)
    down()
    fillcolor(barva)
    begin_fill()
    circle(25)
    end_fill()
    up()
    
def narisiFiguro(barva, x, y):
    up()
    goto(x, y)
    down()
    fillcolor(barva)
    begin_fill()
    circle(10)
    end_fill()
    left(90)
    fd(20)
    bk(10)
    left(90)
    fd(10)
    right(180)
    fd(20)
    up()

def narisiPlosco():
    for x in polja:
        narisiPolje(x.barva, x.x, x.y)

narisiPlosco()

    

    
