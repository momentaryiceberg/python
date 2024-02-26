import keyboard
import pyperclip

expansions = {
    "xcf": "Extra configuration",
    "abc": "Alphabetical",
    # Add more expansions as needed
}

def replace_text():
    # Get the current clipboard contents
    original_text = pyperclip.paste()

    # Check if any expansion matches the typed text
    for word, expansion in expansions.items():
        if original_text.endswith(word):
            # Replace the typed text with the expansion
            new_text = original_text[:-len(word)] + expansion
            pyperclip.copy(new_text)
            break

def main():
    keyboard.add_hotkey("space", replace_text)
    keyboard.wait()

if __name__ == "__main__":
    main()
