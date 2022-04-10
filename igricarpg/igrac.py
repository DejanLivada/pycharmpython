import pygame
from items import *
from pygame.math import Vector2
class Igrac():
    ime = None
    slike =  None
    pozicija = None
    brzina = None
    mana = None
    redni_broj = None
    trenutna_slika = None
    inventory = None
    objective = None
    bullets = None
    pravac = None
    max_mana = None
    trenutno_oruzje = None
    ima_oruzje= None
igrac = Igrac()
igrac.ime = "Owner"
igrac.pravac = 0
igrac.bullets = []
igrac.slike = []
igrac.pozicija = Vector2(50 , 250)
igrac.brzina = 10
igrac.mana = 100
igrac.redni_broj = 0
igrac.slike.append(pygame.image.load("igrac/mis1.png"))
igrac.slike.append(pygame.image.load("igrac/mis2.png"))
igrac.objective = "Open the chest"
igrac.max_mana = 100
igrac.ima_oruzje = False
igrac.inventory = []
