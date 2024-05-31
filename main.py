import json
import os
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

# Load configuration from file if it exists
CONFIG_FILE = 'tibia.config'
if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, 'r') as file:
        config = json.load(file)
else:
    config = {}

if len(config) > 0:
   getFromFile = get_yes_no_input("Carregar configuração salva? S/N")
else:
   getFromFile = False
# Prompt for inputs if not already in config
if 'char' not in config or not getFromFile:
    config['char'] = input("Nome do Char: ")
if 'spellhotkey' not in config or not getFromFile:
    config['spellhotkey'] = input("Hotkey para magia: ")
if 'ringhotkey' not in config or not getFromFile:
    config['ringhotkey'] = input("Hotkey para life ring: ")
if 'foodhotkey' not in config or not getFromFile:
    config['foodhotkey'] = input("Hotkey para comer: ")
if 'Promoted' not in config or not getFromFile:
    config['Promoted'] = get_yes_no_input("Char com promotion? (S/N) ")
if 'Bonus' not in config or not getFromFile:
    config['Bonus'] = get_yes_no_input("Char com bonus semanal de mana? (S/N) ")
if 'blankrunes' not in config or not getFromFile:
    config['blankrunes'] = zeroIfNullInput("Quantidade de blank runes: ")
if 'liferings' not in config or not getFromFile:
    config['liferings'] = zeroIfNullInput("Qtd de life rings: ")
if 'TempoLifeRings' not in config or not getFromFile:
    config['TempoLifeRings'] = zeroIfNullInput("Tempo atual do primeiro life ring (segundos). Deixar em branco se brand new: ")
if 'manaNecessaria' not in config or not getFromFile:
    config['manaNecessaria'] = zeroIfNullInput("Mana necessária para magia: ")
mana = zeroIfNullInput("Mana atual (aproximada): ")

# Save the configuration to a file
with open(CONFIG_FILE, 'w') as file:
    json.dump(config, file, indent=4)

intfcr = Interfacer(foodHotkey=config['foodhotkey'], spellHotkey=config['spellhotkey'], ringHotkey=config['ringhotkey'], charName=config['char'])
sch = Runer(
    promoted=config['Promoted'], 
    lifeRingAmount=config['liferings'], 
    restingBonus=config['Bonus'], 
    blankRunes=config['blankrunes'], 
    requiredMana=config['manaNecessaria'],
    intfcr=intfcr)
sch.setMana(mana)
if config['TempoLifeRings'] > 0:
    sch.setLifeRing(config['TempoLifeRings'])
sch.Start()