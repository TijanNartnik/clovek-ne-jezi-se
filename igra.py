# PROJEKT INFORMATIKA - TIJAN NARTNIK, 1. B
# CLOVEK NE JEZI SE

# uvozimo vse potrebne knjižnjice
from turtle import *
import random
import time

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

# vsa polja kjer so figure na zacetku
baznaPolja = [
    ## rdeca baza
    Polje("red", -400, -400),
    Polje("red", -350, -400),
    Polje("red", -400, -350),
    Polje("red", -350, -350),

    ## rumena baza
    Polje("yellow", 400, -400),
    Polje("yellow", 350, -400),
    Polje("yellow", 400, -350),
    Polje("yellow", 350, -350),

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
]

# polja na sredini - kamor figure prispejo
koncnaPolja = [
   ## rdeca koncna polja
    Polje("red", 25, -275),
    Polje("red", 25, -200), 
    Polje("red", 25, -125),
    Polje("red", 25, -50),

    ## rumena koncna polja
    Polje("yellow", 325, 25),
    Polje("yellow", 250, 25),
    Polje("yellow", 175, 25),
    Polje("yellow", 100, 25),

    ## modra koncna polja
    Polje("blue", 25, 325),
    Polje("blue", 25, 250),
    Polje("blue", 25, 175),
    Polje("blue", 25, 100),

    ## zelena koncna polja
    Polje("green", -275, 25),
    Polje("green", -200, 25),
    Polje("green", -125, 25),
    Polje("green", -50, 25),
]


zacetnoIgralnoPolje = [0, 10, 20, 30]
zacetnoKoncnoPolje = [0, 4, 8, 12]

konec = False
barvaIgralca = "red"

# stevilo figur, ki je prospelo na konec (za vsako barvo)
naKoncu = [
  0,
  0,
  0,
  0
]

# trenutne lokacije figure za vsako barvo, ki je na polju (shranjeni so indexi Polja)
lokacijeFigur = [
  0,
  0,
  0,
  0
]

# funkcija , ki narise polje (krog)
def narisiPolje(barva, x, y):
    up()
    goto(x, y)
    down()
    fillcolor(barva)
    begin_fill()
    circle(25)
    end_fill()
    up()

# funckija, ki narise figuro (malo manjsi krog s krizom)
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
    
# narise gumb na katerega igralec
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

# funkcija, ki narise celotno plosco (s vsemi polji in figurami)
def narisiPlosco():
    # pocisti ekran in pobarvaj na belo, ce se igra ponovno
    clear()
    screen.bgcolor("white")
    goto(0, 0)

    # narisi vsa polja in figure
    for x in igralnaPolja:
      narisiPolje(x.barva, x.x, x.y)
    for x in koncnaPolja:
      narisiPolje(x.barva, x.x, x.y)
    for x in baznaPolja:
      narisiPolje(x.barva, x.x, x.y)
      narisiFiguro(x.barva, x.x, x.y+4)
      
    narisiGumb()

# ko nekdo zmaga ta funkcija prebarva ekran in napise tekst
def zmaga(barva):
    clear()
    screen.bgcolor(barva)
    goto(-600, 0)
    zmagovalec = "Rdeci zmaga! Klikni, ce zelis igrati se enkrat!"
    if barva == "green":
      zmagovalec = "Zeleni zmaga! Klikni, ce zelis igrati se enkrat!"
    elif barva == "blue":
      zmagovalec = "Modri zmaga! Klikni, ce zelis igrati se enkrat!"
    elif barva == "yellow":
      zmagovalec = "Rumeni zmaga! Klikni, ce zelis igrati se enkrat!"
    write(zmagovalec, font=("Verdana", 50, "normal"))

# funkcija ki pretvori barvo v index
def barvaVIndex(barva):
  if barva=="red":
    return 0
  elif barva == "yellow":
    return 1
  elif barva == "blue":
    return 2
  elif barva == "green":
    return 3
  
# funkcija, ki pretvori index v barvo
def indexVBarvo(index):
  if index==0:
    return "red"
  elif index==1:
    return "yellow"
  elif index==2:
    return "blue"
  elif index==3:
    return "green"

# glavna funkcija, ki skrbi ze premike figur
def premakniFiguro(barva, premik):
  global konec
  index = barvaVIndex(barva)

  # dobi index prejsnega polja (pred premikom)
  prejsnoPolje = 0
  if lokacijeFigur[index]-1 > len(igralnaPolja):
    razlika = (lokacijeFigur[index]-2) - len(igralnaPolja) + zacetnoKoncnoPolje[index]
    prejsnoPolje = koncnaPolja[razlika]
  elif lokacijeFigur[index]-1 == len(igralnaPolja):
    prejsnoPolje = igralnaPolja[zacetnoIgralnoPolje[index]]
  else:
    mesto = lokacijeFigur[index]-1 + zacetnoIgralnoPolje[index]
    if mesto > len(igralnaPolja) - 1:
      mesto -= len(igralnaPolja) - 1
    prejsnoPolje = igralnaPolja[mesto]

  # poveca lokacijo figure za premik
  lokacijeFigur[index] = lokacijeFigur[index] + premik
  # pobrise prejsno polje
  narisiPolje(prejsnoPolje.barva, prejsnoPolje.x, prejsnoPolje.y)

  if lokacijeFigur[index]-1 > len(igralnaPolja):
    # figura se premakne v koncno polje
    baznoPolje = lokacijeFigur[index] - len(igralnaPolja) - 2 + zacetnoKoncnoPolje[index]
    x = koncnaPolja[baznoPolje].x
    y = koncnaPolja[baznoPolje].y
    narisiFiguro(barva, x, y+4)
  elif lokacijeFigur[index]-1 == len(igralnaPolja):
    # figura se premakne na prvo polje (zunaj baze)
    x = igralnaPolja[zacetnoIgralnoPolje[index]].x
    y = igralnaPolja[zacetnoIgralnoPolje[index]].y
    narisiFiguro(barva, x, y+4)
  else:
    # figura se premakne normalno
    mesto = lokacijeFigur[index]-1 + zacetnoIgralnoPolje[index]
    if mesto > len(igralnaPolja)-1:
      mesto -= len(igralnaPolja) - 1
    x = igralnaPolja[mesto].x
    y = igralnaPolja[mesto].y
    narisiFiguro(barva, x, y+4)

  # figura je prisla do konca
  if lokacijeFigur[index] == (45-naKoncu[index]):
    lokacijeFigur[index] = 0
    naKoncu[index] += 1
    # na cilju so vse 4 fiure, barva zmaga
    if naKoncu[index] == 4:
      zmaga(barva)
      konec = True
      
        
# preveri ce je pred figuro dovolj prostora za premik, ce ga ni to igralcu napise
def preveriPremik(barva, premik):
  global barvaIgralca
  index = barvaVIndex(barva)
  if (lokacijeFigur[index]+premik) > (45-naKoncu[index]):
    if index == barvaVIndex(barvaIgralca):
      setx(+5)
      write("Ni prostora za premik")
  else:
    premakniFiguro(barva, premik)

# funkcija, ki odigra ostale barve (rumeno, modro, zeleno)
def odigrajOstaleIgralce():
  global barvaIgralca
  igralec = barvaVIndex(barvaIgralca)
  for x in range(3):
    if x != igralec:
      index = x
      x = random.randint(1, 6)
      barva = indexVBarvo(index)
      if lokacijeFigur[index] == 0:
        if x == 6:
          st = naKoncu[index] + 1
          for y in range(st):
            polje = baznaPolja[y+(index*4)]
            narisiPolje(polje.barva, polje.x, polje.y)
          preveriPremik(barva, 1)
      else:
        preveriPremik(barva, x)

# se pozene, ko igralec klike na gumb
def vrziKocko():
  global barvaIgralca
  up()
  x = random.randint(1, 6)
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

  index = barvaVIndex(barvaIgralca)
  print("x, ", barvaIgralca, str(index))
  
  if lokacijeFigur[index] == 0:
    if x < 6:
      setx(+5)
      write("Ni 6 - ne mores iz baze")
    else:
      st = naKoncu[index] + 1
      for x in range(st):
        polje = baznaPolja[x]
        narisiPolje(polje.barva, polje.x, polje.y)
      preveriPremik(barvaIgralca, 1)
    odigrajOstaleIgralce()
  else:
    if x == 6:
      setx(+5)
      write(" - lahko meces se 1krat")
      preveriPremik(barvaIgralca, x)
    else:
      preveriPremik(barvaIgralca, x)
      odigrajOstaleIgralce()

# se pozene ko igralec klikne kamor koli na ekran
def klikNaEkran(x, y):
  # ce je igre konec lahko igralec ponovi igro
  global konec
  if konec:
    # se ena igra
    narisiPlosco()
    konec = False
  else:
    # igra se poteka
    # preveri ce se koordinate klika ujemajo s koordinatami gumba
    if -20 <= x <= 60 and -425 <= y <= -375:
      # gumb je kliknen, vrzi kocko
      vrziKocko()
      
# izbere barvo
def izberiBarvo():
  global barvaIgralca
  pravilno = False

  # ponavlja dokler igralec ne izbere pravilne barve
  while not pravilno:
    b = input("S katero barvo želiš igrati (red, blue, yellow, green)? ")
    if b == "red" or b == "green" or b == "blue" or b == "yellow":
      # izbral je pravilno
      barvaIgralca = b
      pravilno = True
    else:
      # izbral je narobe
      print("Barva ni na voljo!")
  


# igralec si izbere barvo
izberiBarvo()

# narise plosco (igra se lahko zacne)
narisiPlosco()

# spremlja ce je ekran klknjen
screen.onclick(klikNaEkran)
screen.mainloop()
