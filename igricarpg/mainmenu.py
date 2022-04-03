import random

import pygame.math as math
from igrac import *
from UI import *
from tutfiles import *
from items import *
from objectives import *

pygame.init()
Xres = 800
Yres = 600
full_screen = pygame.FULLSCREEN
prozor = pygame.display.set_mode((Xres, Yres) , full_screen)
sat = pygame.time.Clock()
trenutni_ekran = "mainmenu"
def nacrtaj_dugme_bez_centiranja(dugme):
    pygame.draw.rect(prozor, dugme.boja, dugme.rect)
    prozor.blit(dugme.tekst, dugme.rect.topleft)
def fade(width, height):
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        prozor.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(10)


program_radi = True
while program_radi:
    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            program_radi = False
        if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
            if settings_dugme.rect.collidepoint(dogadjaj.pos):
                crtaj_dugmice_mm = False
                trenutni_ekran = "settings"
            if exit_dugme.rect.collidepoint(dogadjaj.pos) and trenutni_ekran == "mainmenu":
                program_radi = False
            if settingstomainmenu.rect.collidepoint(dogadjaj.pos)and trenutni_ekran == "settings":
                trenutni_ekran = "mainmenu"

                crtaj_dugmice_mm = True
            if play_dugme.rect.collidepoint(dogadjaj.pos)and trenutni_ekran == "mainmenu":
                #fade(Xres , Yres)
                trenutni_ekran = "tutorial"

                crtaj_dugmice_mm = False



    dugmici = pygame.key.get_pressed()
    if dugmici[pygame.K_w]:
        igrac.pozicija.y -= igrac.brzina
        igrac.pravac += 6
    if dugmici[pygame.K_s]:
        igrac.pozicija.y += igrac.brzina
        igrac.pravac -= 6
    if dugmici[pygame.K_a]:
        igrac.pozicija.x -= igrac.brzina
        igrac.pravac -= 6
    if dugmici[pygame.K_d]:
        igrac.pozicija.x += igrac.brzina
        igrac.pravac += 6
    if igrac.pozicija.x >= Xres-100:
        igrac.pozicija.x = Xres-100
    if igrac.pozicija.x <= 0:
        igrac.pozicija.x = 0
    if igrac.pozicija.y >= Yres-150:
        igrac.pozicija.y = Yres-150
    if igrac.pozicija.y <= 0:
        igrac.pozicija.y = 0
    if dugmici[pygame.K_ESCAPE]:
        pygame.quit()
        program_radi = False
        

    prozor.fill((0, 0, 0))
    if trenutni_ekran == "mainmenu" or trenutni_ekran== "settings":
        prozor.blit(main_menuslika, (0, 0))
    if trenutni_ekran == "mainmenu" and crtaj_dugmice_mm == True:
        nacrtaj_dugme_bez_centiranja(settings_dugme)
        nacrtaj_dugme_bez_centiranja(exit_dugme)
        nacrtaj_dugme_bez_centiranja(play_dugme)
    if trenutni_ekran == "settings":
        crtaj_dugmice_settings = True
        nacrtaj_dugme_bez_centiranja(settingstomainmenu)
    if trenutni_ekran == "tutorial":
        crtaj_dugmice_tutorial = True
        prozor.blit(tutorial_pozadina , (0,0))
        igrac.trenutna_slika = pygame.transform.scale(igrac.slike[igrac.redni_broj], (100, 100))
        igrac.redni_broj = (igrac.redni_broj + 1) % len(igrac.slike)
        prozor.blit(open_tutorial_chest.header , (433, 99))
        prozor.blit(tutorial_chest.slika, (tutorial_chest.pozicija))
        prozor.blit(igrac.trenutna_slika , (igrac.pozicija))
        if dugmici[pygame.K_b]:
            pygame.draw.rect(prozor ,pygame.Color("lime"), (50,50 , 700,500))
            if open_tutorial_chest.uradjen == False:
                prozor.blit(open_tutorial_chest.ime , (50,50))
        if crtaj_dugmice_tutorial == True and open_tutorial_chest.uradjen == False:
            prozor.blit(tutorial_text , (0,0))
        pygame.time.wait(100)
        if abs(igrac.pozicija.x - tutorial_chest.pozicija.x) <= tutorial_chest.slika.get_width() and abs(igrac.pozicija.y - tutorial_chest.pozicija.y) < tutorial_chest.slika.get_height():
            tutorial_chest.opened = True
            igrac.trenutno_oruzje = basic_wooden_wand.slika
        if dugmici[pygame.K_SPACE] and igrac.mana >= 10  :
            igrac.bullets.append(
                [igrac.pozicija + Vector2(0, 0).rotate(igrac.pravac), igrac.pravac])
           # igrac.bullets.append([igrac.pozicija + Vector2(0, 0).rotate(igrac.pravac),Vector2(10, 0).rotate(igrac.pravac)])
            igrac.mana -= basic_wooden_wand.reqmana
            print(igrac.mana)






    if tutorial_chest.opened == True:
        tutorial_chest.slika = pygame.image.load("chest_opened-removebg-preview.png")
        tutorial_chest.slika = pygame.transform.scale(tutorial_chest.slika, (100, 100))
        prozor.blit(basic_wooden_wand.slika, (tutorial_chest.pozicija.x + 150, tutorial_chest.pozicija.y))
        open_tutorial_chest.uradjen = True
    pygame.display.flip()
    sat.tick(30)

pygame.quit()
