import asyncio
from interfacer import Interfacer
from logging import getLogger
import time

class Runer:
    def __init__(self, promoted, lifeRingAmount, restingBonus, blankRunes, intfcr: Interfacer):
        self.neededMana = 530
        self.promoted = promoted
        self.lifeRingAmount = lifeRingAmount
        self.intfcr = intfcr
        self.restingBonus = restingBonus
        self.baseMulti = 2 if self.restingBonus else 1
        self.CurrentLifeRingTime = 20*60 if self.lifeRingAmount > 0 else 0
        self.baseRestoreTime = 2 if self.promoted else 3
        self.baseRestoreAmount = 2 * self.baseMulti
        self.CurrentCalculatedMana = 0
        self.blankRunes = blankRunes

    def Start(self):
        print(f"[Main] Iniciando...")
        self.intfcr.Eat()
        if self.lifeRingAmount > 0:
            self.intfcr.Ring()
        asyncio.run(self.ScheduleTasks())

    async def schedule_task(self, task, interval):
        while self.blankRunes > 0:
            await task()  # Execute the task
            await asyncio.sleep(interval)  # Wait for the specified interval before scheduling again
        
    async def ScheduleTasks(self):
        time.sleep(3)
        baseRegen_scheduler = self.schedule_task(self.baseManaRegen, self.baseRestoreTime)
        ring_scheduler = self.schedule_task(self.lifeRingRegen, 6)
        check_scheduler = self.schedule_task(self.checkMana, 30)
        eat_scheduler = self.schedule_task(self.intfcr.Eat, 10)

        await asyncio.gather(baseRegen_scheduler, ring_scheduler, check_scheduler, eat_scheduler)

    async def baseManaRegen(self):
        self.CurrentCalculatedMana += self.baseRestoreAmount
        print(f"[Base] Regen Mana: {self.CurrentCalculatedMana}")

    async def lifeRingRegen(self):
        if (self.lifeRingAmount == 0):
            return
        self.CurrentCalculatedMana += 8*self.baseMulti
        print(f"[Ring] Regen Mana: {self.CurrentCalculatedMana}")
        self.CurrentLifeRingTime -= 6
        print(f"[Ring] Time: {self.CurrentLifeRingTime}")
        if (self.CurrentLifeRingTime <= 0):
            self.lifeRingAmount -= 1
            print(f"[Ring] Rings: {self.lifeRingAmount}")
            if self.lifeRingAmount > 0:
                self.CurrentLifeRingTime = 20*60
                self.intfcr.Ring()
    
    def setLifeRing(self, time):
        self.CurrentLifeRingTime = time
    
    def setMana(self, mana):
        self.CurrentCalculatedMana = mana

    async def checkMana(self):
        print(f"[Check] Mana: {self.CurrentCalculatedMana}")
        if self.CurrentCalculatedMana >= self.neededMana:
            self.intfcr.Rune()
            self.blankRunes -= 1
            print(f"[Check] Blank Runes: {self.blankRunes}")
            self.CurrentCalculatedMana -= self.neededMana
