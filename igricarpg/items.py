import pygame
from pygame.math import Vector2

class Wand():
    damage = None
    slika = None
    reqmana = None
    pozicija = None
    crtaj = None


basic_wooden_wand = Wand()
basic_wooden_wand.damage = 10
basic_wooden_wand.slika = pygame.image.load("basicwoodenwatd.jpg")
basic_wooden_wand.slika = pygame.transform.scale(basic_wooden_wand.slika, (80, 80))
basic_wooden_wand.reqmana = 5
basic_wooden_wand.pozicija = Vector2(560, 411)
basic_wooden_wand.crtaj = True