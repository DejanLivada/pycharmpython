import pygame
from pygame.math import Vector2
from items import *
from igrac import *
#++++++++++++++++++++++++++++POCETAK IGRICE+++++++++++++++++++++++

tutorial_pozadina = pygame.image.load("background.jpg")
class Chest():
    slika = None
    sadrzaj = None
    pozicija = None
    opened = None
crtaj_dugmice_tutorial = False
tutorial_chest = Chest()
tutorial_chest.slika = pygame.image.load("chest_closed-removebg-preview.png")
tutorial_chest.slika = pygame.transform.scale(tutorial_chest.slika , (100,100))
tutorial_chest.sadrzaj = basic_wooden_wand.slika
tutorial_chest.opened = False
tutorial_chest.pozicija = Vector2(410,411)
tutorial_font = pygame.font.SysFont("Arial" , 32)
tutorial_text = tutorial_font.render("[???]:Welcome traveler , i left you a chest , try to open it!" ,crtaj_dugmice_tutorial , (0,0,0))
pokupio_prvo_oruzje_text = tutorial_font.render("You just picked up a wooden wand , press 1 to equip it!" , igrac.ima_oruzje , (0,0,0))
