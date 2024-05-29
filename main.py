from interfacer import Interfacer
from scheduler import Runer

char = input("Nome do Char: ")
intfcr = Interfacer(foodHotkey="o", spellHotkey="9", ringHotkey="v", charName=char)
sch = Runer(
    promoted=True, 
    lifeRingAmount=3, 
    restingBonus=True, 
    blankRunes=255, 
    intfcr=intfcr)
sch.setMana(468)
sch.setLifeRing(4*60 + 6)
sch.Start()