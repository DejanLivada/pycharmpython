import pygame

prozor = pygame.display.set_mode((600,600))

R = 280
r = 20
x = 300
y = 300

while R > 50:
    pygame.draw.circle(prozor, (255, 255, 255), (x, y), R, 3)
    R -= r
    x += r

pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()
