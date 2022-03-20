import pygame
from pygame.math import Vector2
import pygame.time
import promeni_res
sat = pygame.time.Clock()
pygame.init()
Xrezolucija = 1920
Yrezolucija = 1080


class Zeaquan():
    slika = None
    pozicija = Vector2(0, Yrezolucija / 2)
    brzina = 0
class Tacka():
    pozicija = None
    boja = pygame.Color("blue")
class Dugme():
    tekst = None
    rect = None
    boja = None
kretanje = False
def nacrtaj_dugme_bez_centiranja(dugme):
    pygame.draw.rect(prozor, dugme.boja, dugme.rect)
    prozor.blit(dugme.tekst, dugme.rect.topleft)
prva_tacka = Tacka()
prva_tacka.pozicija = Vector2(30 , 60)
zeaquan = Zeaquan()
zeaquan.slika = pygame.image.load("jn.jpg")
prozor = pygame.display.set_mode((Xrezolucija, Yrezolucija))
pygame.display.set_caption('Zeaquan Igrica')
zeaquan.slika = pygame.transform.scale(zeaquan.slika, (Xrezolucija / 10, Yrezolucija / 10))
Slika_Pozadina = pygame.image.load("afds.jpg")
Slika_Pozadina = pygame.transform.scale(Slika_Pozadina, (Xrezolucija, Yrezolucija))
druga_tacka = Tacka()
druga_tacka.pozicija = Vector2(20 , Yrezolucija-10)
pygame.display.set_icon(zeaquan.slika)
level = 0
crtaj_pozadinu = False
pomeranje = False
kliktanje = True
dt = 1/30
crtanje_texta = True
faza = 0
a = 10
pomeri_lika = False
program_radi = True
while program_radi:
    if crtaj_pozadinu == True:
        prozor.blit(Slika_Pozadina, (0, 0))
    else:
        pass
    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            program_radi = False
        if dogadjaj.type == pygame.KEYDOWN:
            if dogadjaj.key == pygame.K_ESCAPE:
               promeni_res.menu(Xrezolucija,Yrezolucija)

        if dogadjaj.type == pygame.KEYUP:
            zeaquan.brzina = 0
        if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if kliktanje == False:
                    pass
                else:
                    faza +=1
    tasteri = pygame.key.get_pressed()
    if pomeranje == True:
        prozor.fill((255, 255, 255))
        if tasteri[pygame.K_LEFT]:
            zeaquan.brzina = zeaquan.brzina - a *dt
            zeaquan.pozicija.x = zeaquan.pozicija.x + zeaquan.brzina *dt
        if tasteri[pygame.K_RIGHT]:
            zeaquan.brzina = zeaquan.brzina + a *dt
            zeaquan.pozicija.x = zeaquan.pozicija.x + zeaquan.brzina *dt
        if tasteri[pygame.K_UP]:
            zeaquan.brzina = zeaquan.brzina - a *dt
            zeaquan.pozicija.y = zeaquan.pozicija.y + zeaquan.brzina *dt
        if tasteri[pygame.K_DOWN]:
            zeaquan.brzina = zeaquan.brzina + a *dt
            zeaquan.pozicija.y = zeaquan.pozicija.y + zeaquan.brzina *dt
    else:
        pass

    prozor.blit(zeaquan.slika, (zeaquan.pozicija))
    font_pocni = pygame.font.Font('freesansbold.ttf', 32)
    font_kraj = pygame.font.Font('freesansbold.ttf', 17)
    text_pocni = font_pocni.render('Klikni levo dugme na misu da zapocnes', crtanje_texta, pygame.Color("green"),pygame.Color("blue"))
    text_kraj_animacije = font_kraj.render("Zavrsio si uvodnu animaciju , sada mozes da se kreces po mapi! Pokusaj da  dodjes do Tacke" ,crtanje_texta , pygame.Color("green") )
    text_text2 = font_pocni.render('Zdravo, Ja sam Dejan i ovo je moja igra!', crtanje_texta, pygame.Color("green"), pygame.Color("blue"))
    if zeaquan.pozicija.x <= 0:
        zeaquan.pozicija.x = 0
    if zeaquan.pozicija.y <= 0:
        zeaquan.pozicija.y = 0
    if zeaquan.pozicija.x >= Xrezolucija-zeaquan.slika.get_width():
        zeaquan.pozicija.x = Xrezolucija-zeaquan.slika.get_width()
    if zeaquan.pozicija.y >= Yrezolucija - zeaquan.slika.get_height():
        zeaquan.pozicija.y = Yrezolucija - zeaquan.slika.get_height()
    if faza == 0:
        prozor.blit(text_pocni, (Xrezolucija / 6, Yrezolucija / 2))
        crtaj_pozadinu = True
    if faza == 3:
        prozor.blit(text_text2, (Xrezolucija / 6, Yrezolucija / 3))

    if faza == 2:
        zeaquan.pozicija.x += 1
        if zeaquan.pozicija.x >= Xrezolucija / 2:
            zeaquan.pozicija.x = Xrezolucija / 2
            pomeri_lika = False
    if faza == 4:
        kliktanje = False
        crtaj_pozadinu = False
        prozor.blit(zeaquan.slika, (zeaquan.pozicija))
        pomeranje = True
        prozor.blit(text_kraj_animacije , (0 , 20))
        pygame.draw.circle(prozor , prva_tacka.boja , prva_tacka.pozicija , 20)
        if zeaquan.pozicija.x <= 50 and zeaquan.pozicija.y <= 80:
            level += 1
            faza += 1
            prozor.fill((255, 255, 255))
        if level == 1 and faza == 5:

            pygame.draw.circle(prozor,druga_tacka.boja , druga_tacka.pozicija , 20)




    pygame.display.flip()
    sat.tick(200)