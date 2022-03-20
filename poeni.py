import pygame
from pygame.math import Vector2
import pygame.time


pygame.init()
Xrezolucija = 800
Yrezolucija = 600
prozor = pygame.display.set_mode((Xrezolucija, Yrezolucija))
pygame.display.set_caption('Poeni na dugmice')
mojFont = pygame.font.SysFont('Consolas', 30)
class Dugme:
    tekst = None  # tekst je renderovan tekst (sadrzaj + boja)
    rect = None   # pravougaonik u formatu (x, y, sirina, visina)
    boja = None   # RGB boja pozadine dugmeta


def nacrtaj_dugme_bez_centiranja(dugme):
    pygame.draw.rect(prozor, dugme.boja, dugme.rect)
    prozor.blit(dugme.tekst, dugme.rect.topleft)  # lepsi nacin od linije dole, TOPLEFT je pozicija gornje leve tacke
    # prozor.blit(dugme.tekst, (dugme.rect.x, dugme.rect.y) )

poeni_plus = Dugme()
poeni_plus.boja = pygame.Color("green")
poeni_plus.rect = pygame.Rect(150 , 300 ,200 , 50)
poeni_plus.tekst = mojFont.render("Dodaj poene" , True , (255, 255, 255))
poeni_minus = Dugme()
poeni = 0
poeni_minus.boja = pygame.Color("red")
poeni_minus.rect = pygame.Rect(450 , 300 ,200 , 50)
poeni_minus.tekst = mojFont.render("Oduzmi poene" , True , (255, 255, 255))
font_text = pygame.font.Font('freesansbold.ttf', 32)



program_radi = True
while program_radi:
    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            program_radi = False
        if dogadjaj.type == pygame.KEYDOWN:
            if dogadjaj.key == pygame.K_ESCAPE:
                program_radi = False
        if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if poeni_plus.rect.collidepoint(dogadjaj.pos):
                    poeni += 1
                if poeni_minus.rect.collidepoint(dogadjaj.pos):
                    poeni -= 1
    prozor.fill((0,0,0))
    text_pocni = font_text.render(str(poeni), True, pygame.Color("green"))
    nacrtaj_dugme_bez_centiranja(poeni_plus)
    nacrtaj_dugme_bez_centiranja(poeni_minus)
    prozor.blit(text_pocni , (Xrezolucija/3 , Yrezolucija/4))


    pygame.display.flip()