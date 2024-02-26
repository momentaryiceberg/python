import keyboard

# Þetta gerir manni kleyft að hafa GLOBAL KEYBOARD SHORTCUTS, þýðandi það að glugginn þarf ekki að vera virkur til að triggera function-ið !


def on_key_event(e):
    if e.event_type == keyboard.KEY_DOWN:
        if keyboard.is_pressed("Ctrl+Alt+F"):
            print("Ctrl+Alt+F pressed !! :)")
        elif keyboard.is_pressed("Ctrl+Alt+G"):
            print("Ctrl+Alt+G pressed !! :)")

# hook for key events
keyboard.hook(on_key_event)

# Keep the script running
keyboard.wait('Esc')
