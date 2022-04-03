import pygame


class Wand():
    damage = None
    slika = None
    reqmana = None


basic_wooden_wand = Wand()
basic_wooden_wand.damage = 10
basic_wooden_wand.slika = pygame.image.load("basicwoodenwatd.jpg")
basic_wooden_wand.slika = pygame.transform.scale(basic_wooden_wand.slika, (80, 80))
basic_wooden_wand.reqmana = 5
