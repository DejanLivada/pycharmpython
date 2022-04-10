import pygame
from pygame.math import Vector2
pygame.init()
Xres = 800
Yres = 600
prozor = pygame.display.set_mode((Xres,Yres))

crtaj_main_menu = True
class Dugme:
    tekst = None  # tekst je renderovan tekst (sadrzaj + boja)
    slika = None   # RGB boja pozadine dugmeta
    pozicija = None
def nacrtaj_dugme_bez_centiranja(dugme):
    prozor.blit(dugme.slika , (dugme.pozicija))
    prozor.blit(dugme.tekst, dugme.pozicija )
mojFont = pygame.font.SysFont('Consolas', 30)
start_dugme = Dugme()
start_dugme.pozicija = Vector2(Xres/2 , Yres/2)
start_dugme.tekst = mojFont.render("Start" , crtaj_main_menu , (255,255,255))
start_dugme.slika = pygame.image.load("dugme_background.png")
