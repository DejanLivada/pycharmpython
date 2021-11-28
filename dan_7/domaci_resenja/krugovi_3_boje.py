import pygame

prozor = pygame.display.set_mode((600,600))

centar = (300,300)
r = 20
boja = 0

while r < 260:
    if boja == 0:
        pygame.draw.circle(prozor, (0,255,0), centar, r, 2)
    elif boja == 1:
        pygame.draw.circle(prozor, (0, 0, 255), centar, r, 2)
    else:
        pygame.draw.circle(prozor, (255, 0, 0), centar, r, 2)

    r = r + 20

    boja = (boja + 1) % 3
    """
    boja = boja + 1
    if boja == 3:
        boja = 0
    """

pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()