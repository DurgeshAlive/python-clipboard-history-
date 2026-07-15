import time
import keyboard
import pyperclip

history = []

def show_history():
    print("\n--- Clipboard History ---")
    for item in history[-5:]:
        print("-", item)
    print("-------------------------\n")

keyboard.add_hotkey('ctrl+alt+h', show_history)

print("Monitoring started... Press Ctrl+Alt+H to see history.")
last_item = ""

while True:
    current_item = pyperclip.paste()
    if current_item != last_item and current_item.strip() != "":
        last_item = current_item
        history.append(current_item)
        
        with open("history.txt", "a", encoding="utf-8") as file:
            file.write(current_item + "\n")
            
        print("Saved:", current_item[:30])
        
    time.sleep(1)