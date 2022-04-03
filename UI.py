import pygame
pygame.init()

#*************************DEFINISEM DUGME************************#
class Dugme:
    tekst = None  # tekst je renderovan tekst (sadrzaj + boja)
    rect = None   # pravougaonik u formatu (x, y, sirina, visina)
    boja = None   # RGB boja pozadine dugmeta


#**************************MAIN MENU******************************+#
main_menuslika = pygame.image.load("pxArt.png")
main_menufont = pygame.font.SysFont("Comic Sans MS" , 32)
crtaj_dugmice_mm = True
crtaj_dugmice_settings = False

settings_dugme = Dugme() # definisem settings dugme
settings_dugme.tekst = main_menufont.render("Settings" , crtaj_dugmice_mm , (43, 255, 0))
settings_dugme.rect = pygame.Rect(50, 600 / 2, 140, 50)
settings_dugme.boja = (46, 48, 48)
play_dugme  = Dugme() #definisem dugme koje pokrece igricu
play_dugme.rect =pygame.Rect(50, 200 , 140,50)
play_dugme.tekst = main_menufont.render("Play" , crtaj_dugmice_mm , (43,255,0))
play_dugme.boja = (46,48,48)
exit_dugme = Dugme()# exit dugme
exit_dugme.tekst = main_menufont.render("Exit" , crtaj_dugmice_mm , (43,255,0))
exit_dugme.rect = pygame.Rect(50 , 396 , 140,50)
exit_dugme.boja = (46,48,48)
settingstomainmenu = Dugme()#ako si u settingsu , ovo je back dugme
settingstomainmenu.rect = pygame.Rect(24, 481 , 100,50)
settingstomainmenu.tekst = main_menufont.render("Back" ,crtaj_dugmice_settings, (255,255,255))
settingstomainmenu.boja = (46,48,48)
changelogs_dugme = Dugme()#definisem change logs dugme

#*****************************-----------*******************************

