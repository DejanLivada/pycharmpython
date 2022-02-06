import pygame

pygame.init()
prozor = pygame.display.set_mode((600,600))
sat = pygame.time.Clock()
prozor.fill((0,0,0))


boja = "white"

# na tastaturi
# w - white
# r - red
# g - green
# b - blue
lista_pozicija = []
program_radi = True
while program_radi:
    x,y = pygame.mouse.get_pos()
    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            pygame.image.save(prozor, "slika.png")
            program_radi = False
        if dogadjaj.type == pygame.KEYDOWN:
            if dogadjaj.key == pygame.K_w:
                boja = "white"
            if dogadjaj.key == pygame.K_r:
                boja = "red"
            if dogadjaj.key == pygame.K_g:
                boja = "green"
            if dogadjaj.key == pygame.K_b:
                boja = "blue"

    if pygame.mouse.get_pressed()[0]:
        lista_pozicija.append((x , y))
        if len(lista_pozicija) == 1:
            pygame.draw.circle(prozor, pygame.Color(boja), (x, y), 5)
        else:
            pygame.draw.line(prozor, pygame.Color(boja), lista_pozicija[-1], lista_pozicija[-2], 5)
    if not pygame.mouse.get_pressed()[0]:
        lista_pozicija = []

    if pygame.mouse.get_pressed()[2]:
        pygame.draw.circle(prozor, pygame.Color("black"),(x , y), 5)

    # arr = [4, 8, 10]
    # len(arr) -> 3
    # arr[len(arr)-1] == arr[-1]


    pygame.display.flip()
    sat.tick(30)

pygame.quit()
