import pyperclip

# Pastes from clipboard with spaces removed
def paste_and_remove_spaces():
    # Get clipboard contents
    clipboard_content = pyperclip.paste()
    # Remove spaces from the content
    content_without_spaces = clipboard_content.replace(' ', '')
    return content_without_spaces

def fletta_ja_numer():
    # https://ja.is/?q=5151111
    return paste_and_remove_spaces()

# print(pyperclip.paste())


print(fletta_ja_numer())

