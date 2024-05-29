import pyautogui
import win32gui


class Interfacer:
    def __init__(self, foodHotkey, spellHotkey, ringHotkey, charName):
        self.foodHotkey = foodHotkey
        self.spellHotkey = spellHotkey
        self.ringHotkey = ringHotkey
        self.WindowName = f"Tibia - {charName}"
        self.hwnd= win32gui.FindWindow(None, f"Tibia - {charName}")

    async def Eat(self):
        win32gui.ShowWindow(self.hwnd, 5)
        pyautogui.press("alt")
        win32gui.SetForegroundWindow(self.hwnd)  # Activate the window
        pyautogui.press(self.foodHotkey)

    def Rune(self):
        win32gui.ShowWindow(self.hwnd, 5)
        pyautogui.press("alt")
        win32gui.SetForegroundWindow(self.hwnd)  # Activate the window
        pyautogui.press(self.spellHotkey)

    def Ring(self):
        win32gui.ShowWindow(self.hwnd, 5)
        pyautogui.press("alt")
        win32gui.SetForegroundWindow(self.hwnd)  # Activate the window
        pyautogui.press(self.ringHotkey)