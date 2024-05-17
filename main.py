from interfacer import Interfacer
from scheduler import Runer
import asyncio

intfcr = Interfacer("o", spellHotkey="9", ringHotkey="v", charName="Luis Paulo Style")
sch = Runer(
    promoted=True, 
    lifeRingAmount=2, 
    restingBonus=False, 
    blankRunes=296, 
    intfcr=intfcr)
sch.setMana(338)
sch.setLifeRing(17*60 + 42)
sch.Start()