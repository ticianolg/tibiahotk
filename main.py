from interfacer import Interfacer
from scheduler import Runer

def get_yes_no_input(message):
  """Gets user input (S/N) case-insensitively.

  Args:
      message: The message to display to the user.

  Returns:
      True if the user enters 's' or 'S', False otherwise.
  """

  while True:
    user_input = input(f"{message} (S/N): ").lower()  # Convert to lowercase
    if user_input in ('s', 'n'):
      return user_input == 's'  # Return True for 'y'
    else:
      print("Entrada inválida. Por favor entrar S ou N.")

def zeroIfNullInput(message):
  user_input = input(message)
  if not user_input:
    return 0
  else:
    return int(user_input)

char = input("Nome do Char: ")
spellhotkey = input("Hotkey para magia: ")
ringhotkey = input("Hotkey para life ring: ")
foodhotkey = input("Hotkey para comer: ")
Promoted = get_yes_no_input("Char com promotion? (S/N) ")
Bonus = get_yes_no_input("Char com bonus semanal de mana? (S/N) ")
blankrunes = zeroIfNullInput("Quantidade de blank runes: ")
liferings = zeroIfNullInput("Qtd de life rings: ")
TempoLifeRings = zeroIfNullInput("Tempo atual do primeiro life ring (segundos). Deixar em branco se brand new: ")
mana = zeroIfNullInput("Mana atual (aproximada): ")

intfcr = Interfacer(foodHotkey=foodhotkey, spellHotkey=spellhotkey, ringHotkey=ringhotkey, charName=char)
sch = Runer(
    promoted=Promoted, 
    lifeRingAmount=liferings, 
    restingBonus=Bonus, 
    blankRunes=blankrunes, 
    intfcr=intfcr)
sch.setMana(mana)
if TempoLifeRings > 0:
    sch.setLifeRing(4*60 + 6)
sch.Start()