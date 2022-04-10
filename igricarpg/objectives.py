import pygame
from tutfiles import *


class Objective:
    ime = None
    header = tutorial_font.render("HOLD TAB to open objectives tab!" , crtaj_dugmice_tutorial  , (0,0,0))
    uradjen = None
    pozadina = None
broj_objectiva = 1

open_tutorial_chest = Objective()

open_tutorial_chest.ime = tutorial_font.render(f"{broj_objectiva}.Open the chest!" , crtaj_dugmice_tutorial  , (0,0,0))
open_tutorial_chest.uradjen = False
equip_wooden_wand = Objective()
equip_wooden_wand.ime = tutorial_font.render(f"{broj_objectiva}.Equip your weapon!", crtaj_dugmice_tutorial , (0,0,0))
equip_wooden_wand.uradjen = False


