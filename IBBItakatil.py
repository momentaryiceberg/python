import os
import sys
import win32con
import win32gui
import win32api
import time

from threading import Thread

DOWNLOADS_FOLDER = os.path.join(os.path.expanduser('~'), 'Downloads')
FOLDER_A = os.path.join(DOWNLOADS_FOLDER, 'A')
FOLDER_B = os.path.join(DOWNLOADS_FOLDER, 'B')

def move_file_to_folder(file_path, folder_path):
    try:
        os.makedirs(folder_path, exist_ok=True)
        file_name = os.path.basename(file_path)
        destination = os.path.join(folder_path, file_name)
        os.rename(file_path, destination)
        print(f"Moved {file_name} to {folder_path}")
    except Exception as e:
        print(f"Error moving file: {e}")

def get_selected_file_path():
    window = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(window)
    if "File Explorer" in title:
        selected_files = win32gui.SendMessage(window, win32con.WM_COPYDATA, 0, "SelectedItems")
        data = win32gui.SendMessage(window, win32con.WM_GETTEXTLENGTH, 0, None)
        buffer = win32gui.PyMakeBuffer(data)
        win32gui.SendMessage(window, win32con.WM_GETTEXT, data, buffer)
        return buffer.tobytes().decode('utf-16') if selected_files else None
    return None

def monitor_keyboard():
    while True:
        if win32api.GetAsyncKeyState(win32con.VK_ESCAPE) & 0x8000:
            print("Exiting...")
            break
        elif win32api.GetAsyncKeyState(ord('1')) & 0x8000:
            file_path = get_selected_file_path()
            if file_path:
                move_file_to_folder(file_path.strip(), FOLDER_A)
        elif win32api.GetAsyncKeyState(ord('2')) & 0x8000:
            file_path = get_selected_file_path()
            if file_path:
                move_file_to_folder(file_path.strip(), FOLDER_B)
        time.sleep(0.1)

def main():
    print("Starting background file mover...")
    print("Press '1' to move the currently selected file to Folder A")
    print("Press '2' to move the currently selected file to Folder B")
    print("Press 'Esc' to exit")

    thread = Thread(target=monitor_keyboard)
    thread.daemon = True
    thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()
