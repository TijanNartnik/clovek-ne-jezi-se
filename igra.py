# PROJEKT INFORMATIKA - TIJAN NARTNIK, 1. B
# CLOVEK NE JEZI SE

from turtle import *

# pohitrimo turtle
speed(150)

class Polje:
  def __init__(self, barva, x, y):
    self.barva = barva
    self.x = x
    self.y = y

## vsa igralna polja
    # TODO: uredi array po vrsti in loci med baznimi polji in igralnimi polji
polja = [
    ## rdeca baza
    Polje("red", -400, -400),
    Polje("red", -350, -400),
    Polje("red", -400, -350),
    Polje("red", -350, -350),

    ## modra baza
    Polje("blue", 400, 400),
    Polje("blue", 350, 400),
    Polje("blue", 400, 350),
    Polje("blue", 350, 350),

    ## zelena baza
    Polje("green", -400, 400),
    Polje("green", -350, 400),
    Polje("green", -400, 350),
    Polje("green", -350, 350),

    ## rumena baza
    Polje("yellow", 400, -400),
    Polje("yellow", 350, -400),
    Polje("yellow", 400, -350),
    Polje("yellow", 350, -350),

    ## rdeca koncna polja
    Polje("red", 25, -50),
    Polje("red", 25, -125),
    Polje("red", 25, -200),
    Polje("red", 25, -275),

    ## modra koncna polja
    Polje("blue", 25, 100),
    Polje("blue", 25, 175),
    Polje("blue", 25, 250),
    Polje("blue", 25, 325),

    ## rumena koncna polja
    Polje("yellow", 100, 25),
    Polje("yellow", 175, 25),
    Polje("yellow", 250, 25),
    Polje("yellow", 325, 25),

    ## zelena koncna polja
    Polje("green", -50, 25),
    Polje("green", -125, 25),
    Polje("green", -200, 25),
    Polje("green", -275, 25),

    ## bela polja (in barvna startna polja
    Polje("red", -50, -350),
    Polje("white", 25, -350),
    Polje("white", 100, -350),

    Polje("white", 100, -275),
    Polje("white", 100, -200),
    Polje("white", 100, -125),
    Polje("white", 100, -50),

    Polje("white", 175, -50),
    Polje("white", 250, -50),
    Polje("white", 325, -50),

    Polje("yellow", 400, -50),
    Polje("white", 400, 25),
    Polje("white", 400, 100),

    Polje("white", 325, 100),
    Polje("white", 250, 100),
    Polje("white", 175, 100),
    Polje("white", 100, 100),

    Polje("white", 100, 175),
    Polje("white", 100, 250),
    Polje("white", 100, 325),
    Polje("blue", 100, 400),

    Polje("white", 25, 400),
    Polje("white", -50, 400),
    
    Polje("white", -50, 325),
    Polje("white", -50, 250),
    Polje("white", -50, 175),
    Polje("white", -50, 100),

    Polje("white", -125, 100),
    Polje("white", -200, 100),
    Polje("white", -275, 100),
    Polje("green", -350, 100),

    Polje("white", -350, 25),
    Polje("white", -350, -50),

    Polje("white", -275, -50),
    Polje("white", -200, -50),
    Polje("white", -125, -50),
    Polje("white", -50, -50),

    Polje("white", -50, -125),
    Polje("white", -50, -200),
    Polje("white", -50, -275),    
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
