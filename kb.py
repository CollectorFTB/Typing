import threading

from pynput.keyboard import Key, Listener


class KBListener(Listener):
    def __init__(self):
        self.log_file = open('log.txt','a')
        def on_press(key):
            char = key_to_char(key)
            self.log_file.write(char) # save in file
            print(char, end='', flush=True) # print to console

        def on_release(key):
            if key == Key.esc:
                self.log_file.close()
                return False
        
        super().__init__(on_press=on_press, on_release=on_release)

    def start(self):
        Listener.start(self)
        self.join()

def key_to_char(key):
    try:
        char = key.char
    except AttributeError:
        if key == Key.space:
            char = ' '
        elif key == Key.enter:
            char = '\n'
        # elif key == Key.backspace:
        #     char = '\b'
        else:
            char = ''
    return char
