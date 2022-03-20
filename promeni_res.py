import pygame
import pygame.time

pygame.init()

def menu(Xrezolucija,Yrezolucija):

    mojFont = pygame.font.Font('freesansbold.ttf', 32)
    prozor = pygame.display.set_mode((Xrezolucija , Yrezolucija))
    pygame.display.set_caption('Menjanje rezolucije u igri')

    class Dugme800x600:
        def __init__(self, tekst,boja):
            self.tekst=mojFont.render(tekst, True, (255, 255, 255))  # tekst je renderovan tekst (sadrzaj + boja)
            self.rect = pygame.Rect(Xrezolucija - 200, Yrezolucija / 2, 200, 50)  # pravougaonik u formatu (x, y, sirina, visina)
            self.boja = pygame.Color(boja)   # RGB boja pozadine dugmeta

    class Dugme1600x1200:
        def __init__(self, tekst, boja):
            self.tekst = mojFont.render(tekst, True, (255, 255, 255))  # tekst je renderovan tekst (sadrzaj + boja)
            self.rect = pygame.Rect(Xrezolucija / 2 - 100 , Yrezolucija / 2, 200, 50)
            self.boja = pygame.Color(boja)  # RGB boja pozadine dugmeta

    class Dugme1920x1080:
        def __init__(self, tekst, boja):
            self.tekst = mojFont.render(tekst, True, (255, 255, 255))  # tekst je renderovan tekst (sadrzaj + boja)
            self.rect = pygame.Rect(0, Yrezolucija / 2, 200, 50)
            self.boja = pygame.Color(boja)  # RGB boja pozadine dugmeta

    class DugmePaliGasiFullScreen:
        def __init__(self, tekst, boja):
            self.tekst = mojFont.render(tekst, True, (255, 255, 255))  # tekst je renderovan tekst (sadrzaj + boja)
            self.rect =  pygame.Rect(Xrezolucija/2 - 100 , 0 , 300 , 50)
            self.boja = pygame.Color(boja)  # RGB boja pozadine dugmeta
    class IzadjiIzIgre:
        def __init__(self, tekst, boja):
            self.tekst = mojFont.render(tekst, True, (255, 255, 255))  # tekst je renderovan tekst (sadrzaj + boja)
            self.rect =  pygame.Rect(Xrezolucija/2 - 100 , Yrezolucija/1.2 , 200 , 50)
            self.boja = pygame.Color(boja)  # RGB boja pozadine dugmeta

    def nacrtaj_dugme_bez_centiranja(dugme):
        pygame.draw.rect(prozor, dugme.boja, dugme.rect)
        prozor.blit(dugme.tekst, dugme.rect.topleft)
    fullscreen = True
    program_radi = True
    while program_radi:
        prozor.fill((0,0,0))
        text_upozorenje = mojFont.render('UPOZORENJE! UKLJUCI Fullscreen pa promeni rezoluciju ', True, pygame.Color("red"),pygame.Color("black"))

        fullScreenDugme = DugmePaliGasiFullScreen("Fullscreen:"+ str(fullscreen), "cyan")
        dugme800x600 = Dugme800x600("800 x 600", "red")
        dugme1600x1200 = Dugme1600x1200("1600 x 1200", "green")
        dugme1920x1080 = Dugme1920x1080("1920 x 1080","blue")
        izadjiizigre = IzadjiIzIgre("Izadji iz igre" , "gray")
        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                program_radi = False
            if dogadjaj.type == pygame.KEYDOWN:
                if dogadjaj.key == pygame.K_ESCAPE:
                    program_radi = False
            if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if fullScreenDugme.rect.collidepoint(dogadjaj.pos):
                        fullscreen = not fullscreen
                        if fullscreen == False:
                            pygame.display.quit()
                            pygame.display.init()
                            prozor = pygame.display.set_mode((Xrezolucija , Yrezolucija))
                        else:
                            pygame.display.quit()
                            pygame.display.init()
                            prozor = pygame.display.set_mode((Xrezolucija , Yrezolucija), pygame.FULLSCREEN)
                    if dugme800x600.rect.collidepoint(dogadjaj.pos):
                        Xrezolucija = 800
                        Yrezolucija = 600
                        if fullscreen == True:
                            prozor = pygame.display.set_mode((Xrezolucija ,Yrezolucija) , pygame.FULLSCREEN)
                        if fullscreen == False:
                            prozor = pygame.display.set_mode((Xrezolucija, Yrezolucija))
                    if dugme1600x1200.rect.collidepoint(dogadjaj.pos):
                        Xrezolucija = 1600
                        Yrezolucija = 1200
                        if fullscreen == True:
                            prozor = pygame.display.set_mode((Xrezolucija ,Yrezolucija) , pygame.FULLSCREEN)
                        else:
                            prozor = pygame.display.set_mode((Xrezolucija, Yrezolucija))
                    if dugme1920x1080.rect.collidepoint(dogadjaj.pos):
                        Xrezolucija = 1920
                        Yrezolucija = 1080
                        if fullscreen == True:
                            prozor = pygame.display.set_mode((Xrezolucija ,Yrezolucija) , pygame.FULLSCREEN)
                        else:
                            prozor = pygame.display.set_mode((Xrezolucija, Yrezolucija))
                    if izadjiizigre.rect.collidepoint(dogadjaj.pos):
                        pygame.quit()


        nacrtaj_dugme_bez_centiranja(dugme800x600)
        nacrtaj_dugme_bez_centiranja(dugme1600x1200)
        nacrtaj_dugme_bez_centiranja(dugme1920x1080)
        nacrtaj_dugme_bez_centiranja(fullScreenDugme)
        nacrtaj_dugme_bez_centiranja(izadjiizigre)
        prozor.blit(text_upozorenje , (Xrezolucija / 2 - 400 , Yrezolucija/3))
        pygame.display.flip()