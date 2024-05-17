from interfacer import Interfacer
from scheduler import Runer
import asyncio

intfcr = Interfacer(foodHotkey="o", spellHotkey="9", ringHotkey="v", charName="Luis Paulo Style")
sch = Runer(
    promoted=True, 
    lifeRingAmount=3, 
    restingBonus=True, 
    blankRunes=264, 
    intfcr=intfcr)
sch.setMana(551)
sch.setLifeRing(16*60 + 46)
sch.Start()