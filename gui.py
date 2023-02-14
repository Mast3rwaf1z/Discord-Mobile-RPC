import os
from pynput.keyboard import Listener, Key
from time import sleep

width = os.get_terminal_size().columns
print_right = lambda o: print(f'\033[C'*(width-len(o))+o, end='')
running = True


def connect():
    pass

def scan():
    pass

def stop():
    global running
    running = False
    print()
    

actions:list[dict] = [
    {"Connect":connect},
    {"Scan for games":scan},
    {"Exit":stop}
]

index = len(actions)-1

def on_press(key:Key):
    global index
    match key:
        case Key.enter:
            actions[index][next(iter(actions[index].keys()))]()
        case Key.up:
            if index == 0:
                return
            index-=1
            print("\t)\033[A\r\t>", end='\r')
        case Key.down:
            if index == len(actions)-1:
                return
            index+=1
            print("\t)\033[B\r\t>", end='\r')
def run():
    global running
    listener = Listener(on_press=on_press, suppress=True)
    listener.start()
    print("_"*width)
    print_right(str(index)+'\n')
    print('\r', end='')
    for action in actions:
        print("\t) "+next(iter(action.keys())))
    print("\033[A\t> ", end='\r')
    while running: sleep(1)