import User_Interface

User_Interface.pygame.init()
sat = User_Interface.pygame.time.Clock()

program_radi = True
while program_radi:
    for dogadjaj in User_Interface.pygame.event.get():
        if dogadjaj.type == User_Interface.pygame.QUIT:
            program_radi = False
        if dogadjaj.type == User_Interface.pygame.MOUSEBUTTONDOWN:
            if User_Interface.start_dugme.slika.get_rect().collidepoint(dogadjaj.pos):
                print("radi")
                print(User_Interface.start_dugme.slika.get_rect())

    User_Interface.prozor.fill((0, 0, 0))

    User_Interface.nacrtaj_dugme_bez_centiranja(User_Interface.start_dugme)
    User_Interface.pygame.display.flip()
    sat.tick(30)

User_Interface.pygame.quit()