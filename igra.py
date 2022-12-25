# PROJEKT INFORMATIKA - TIJAN NARTNIK, 1. B
# CLOVEK NE JEZI SE

from turtle import *
import random

screen = Screen()

# pohitrimo turtle
speed(150)

class Polje:
  def __init__(self, barva, x, y):
    self.barva = barva
    self.x = x
    self.y = y

class Figura:
  def __init__(self, barva, x, y):
    self.barva = barva
    self.x = x
    self.y = y

## vsa igralna polja
igralnaPolja = [
    ## bela polja (in barvna startna polja)
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

baznaPolja = [
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
]

koncnaPolja = [
   ## rdeca koncna polja
    Polje("red", 25, -275),
    Polje("red", 25, -200), 
    Polje("red", 25, -125),
    Polje("red", 25, -50),

    ## modra koncna polja
    Polje("blue", 25, 325),
    Polje("blue", 25, 250),
    Polje("blue", 25, 175),
    Polje("blue", 25, 100),

    ## rumena koncna polja
    Polje("yellow", 325, 25),
    Polje("yellow", 250, 25),
    Polje("yellow", 175, 25),
    Polje("yellow", 100, 25),

    ## zelena koncna polja
    Polje("green", -275, 25),
    Polje("green", -200, 25),
    Polje("green", -125, 25),
    Polje("green", -50, 25),
]

rdeceZacetnoPolje = 0
rumenoZacetnoPolje = 10
modroZacetnoPolje = 20
zelenoZacetnoPolje = 30

naKoncu = [
  0,
  0,
  0,
  0
]

# 0 - redeci, 1 - rumeni, 2 - modri, 3 - zeleni
naPotezi = 0
premik = 0
lokacijeFigur = [
  0,
  0,
  0,
  0
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
    width(2)
    down()
    fillcolor(barva)
    begin_fill()
    circle(20)
    end_fill()
    left(90)
    fd(40)
    bk(20)
    left(90)
    fd(20)
    right(180)
    fd(40)
    width(1)
    up()
    

def narisiGumb():
    up()
    goto(-20, -425)
    down()
    fillcolor("gray")
    begin_fill()
    for _ in range(2):
      forward(80)
      left(90)
      forward(40)
      left(90)
    end_fill()
    up()
    goto(-15, -400)
    write("Vrzi Kocko")


def narisiPlosco():
    for x in igralnaPolja:
      narisiPolje(x.barva, x.x, x.y)
    for x in koncnaPolja:
      narisiPolje(x.barva, x.x, x.y)
    for x in baznaPolja:
      narisiPolje(x.barva, x.x, x.y)
      narisiFiguro(x.barva, x.x, x.y+4)
    narisiGumb()


def zmaga(barva):
    clear()
    screen.bgcolor(barva)
    goto(-250, 0)
    zmagovalec = "Rdeci zmaga!"
    if barva == "green":
      zmagovalec = "Zeleni zmaga!"
    elif barva == "blue":
      zmagovalec = "Modri zmaga!"
    elif barva == "yellow":
      zmagovalec = "Rumeni zmaga!"
    write(zmagovalec, font=("Verdana", 50, "normal"))


def premakniFiguro(barva, premik):
  if barva=="red":
    prejsnoPolje = 0
    if lokacijeFigur[0]-1 > len(igralnaPolja):
      razlika = (lokacijeFigur[0]-2) - len(igralnaPolja)
      prejsnoPolje = koncnaPolja[razlika]
    elif lokacijeFigur[0]-1 == len(igralnaPolja):
      prejsnoPolje = igralnaPolja[0]
    else:
      prejsnoPolje = igralnaPolja[lokacijeFigur[0]-1]

    lokacijeFigur[0] = lokacijeFigur[0]+premik
    print(prejsnoPolje.barva, prejsnoPolje.x, prejsnoPolje.y)
    narisiPolje(prejsnoPolje.barva, prejsnoPolje.x, prejsnoPolje.y)
    print(premik, lokacijeFigur[0])
    
    if lokacijeFigur[0]-1 > len(igralnaPolja):
      baznoPolje = lokacijeFigur[0] - len(igralnaPolja) - 2
      print(baznoPolje)
      x = koncnaPolja[baznoPolje].x
      y = koncnaPolja[baznoPolje].y
      print("v enki")
      narisiFiguro(barva, x, y+4)
    elif lokacijeFigur[0]-1 == len(igralnaPolja):
      x = igralnaPolja[0].x
      y = igralnaPolja[0].y
      print("v dvojki")
      narisiFiguro(barva, x, y+4)
    else:
      x = igralnaPolja[lokacijeFigur[0]-1].x
      y = igralnaPolja[lokacijeFigur[0]-1].y
      print("v trojki")
      narisiFiguro(barva, x, y+4)

    ## figura je prisla do konca
    if lokacijeFigur[0] == (45-naKoncu[0]):
      lokacijeFigur[0] = 0
      naKoncu[0] += 1
      if naKoncu[0] == 4:
        zmaga(barva)
        


def preveriPremik(barva, premik):
  if barva == "red":
    if (lokacijeFigur[0]+premik) > (45-naKoncu[0]):
      setx(+5)
      write("Ni prostora za premik")
    else:
      premakniFiguro(barva, premik)


def vrziKocko():
  up()
  x = random.randint(1, 6)
  print(x)
  premik = x
  # pocisti ta del platna
  goto(-20, -460)
  down()
  fillcolor("white")
  begin_fill()
  for _ in range(2):
    forward(140)
    left(90)
    forward(20)
    left(90)
  end_fill()
  up()
  goto(-10, -460)
  write(x)
  up()
  if lokacijeFigur[0] == 0:
    if x < 6:
      setx(+5)
      write("Ni 6 - ne mores iz baze")
    else:
      st = naKoncu[0] + 1
      for x in range(st):
        polje = baznaPolja[x]
        narisiPolje(polje.barva, polje.x, polje.y)
      preveriPremik("red", 1)
  else:
    preveriPremik("red", x)


def klikGumba(x, y):
  if -20 <= x <= 60 and -425 <= y <= -375:
    vrziKocko()
      
    

narisiPlosco()
screen.onclick(klikGumba)
screen.mainloop()
