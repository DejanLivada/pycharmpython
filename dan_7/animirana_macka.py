import pygame

prozor = pygame.display.set_mode((600, 600))

slike = []
slike.append( pygame.image.load("macka_puca/shooting_1.png") )
slike.append( pygame.image.load("macka_puca/shooting_2.png") )
slike.append( pygame.image.load("macka_puca/shooting_3.png") )
slike.append( pygame.image.load("macka_puca/shooting_4.png") )
slike.append( pygame.image.load("macka_puca/shooting_5.png") )
slike.append( pygame.image.load("macka_puca/shooting_6.png") )
slike.append( pygame.image.load("macka_puca/shooting_7.png") )

redni_broj = 0
while True:
    prozor.fill((0,0,0))
    trentuna_slika = pygame.transform.scale(slike[redni_broj], (300, 200))
    redni_broj = (redni_broj + 1) % len(slike)
    prozor.blit(trentuna_slika, (50,50))
    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()

