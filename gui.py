import os
from pynput.keyboard import Listener, Key
from time import sleep
from threading import Thread
import subprocess

from Arcaea import Arcaea
from ProjectSekai import ProjectSekai
import Config
import Discord

width = os.get_terminal_size().columns
print_right = lambda o: print(f'\033[C'*(width-len(o))+o, end='\r')
running = True
config = Config.read()


def connect():
        if config["connection_type"] == "wireless":
            while True:
                for dots in [".", "..", "..."]:
                    print_top_right("Scanning"+dots+"  ")
                    sleep(1)
                    response = subprocess.check_output(["adb", "connect", f'{config["ip"]}:{config["port"]}'])
                    if response == f'connected to {config["ip"]}:{config["port"]}' or f'already connected to {config["ip"]}:{config["port"]}':
                        print("\033[32m", end="")
                        print_top_right("Device Connected")
                        print("\033[0m", end="")
                        return

        else:
            print("\033[32m", end="")
            print_top_right("Device Connected")
            print("\033[0m", end="")

def scan():
    game = None
    while game is None:
        for dots in [".", "..", "..."]:
            print_top_left("Scanning"+dots+"  ")
            status = subprocess.check_output(["adb", "shell", "dumpsys", "window", "|", "grep", "mCurrentFocus"])
            match status.decode().split("u0 ")[1].split("/")[0]:
                case Arcaea.name:
                    game = Arcaea()
                    break
                case ProjectSekai.name:
                    game = ProjectSekai()
                    break
            sleep(1)
    print_top_left(f"\033[32mGame: {game.displayName}\033[0m")
    Discord.main(game)
    scan()

def stop():
    global running
    running = False
    

actions:list[dict] = [
    {"Connect":connect},
    {"Scan for games":scan},
    {"Exit":stop}
]

index = len(actions)-1
print_top_right = lambda o: print(("\033[A"*(index+1))+("\033[C"*int(width/2))+(' '*(int(width/2)-len(o)))+o+("\033[B"*(index)))
print_top_left = lambda o: print(("\033[A"*(index+1))+o+(' '*(int(width/2)-len(o)))+("\033[B"*(index)))

def on_press(key:Key):
    global index
    match key:
        case Key.enter:
            Thread(target=actions[index][next(iter(actions[index].keys()))], daemon=True).start()
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
    print("\033[33m"+("_"*width)+"\n\033[0m")
    print('\r', end='')
    for action in actions:
        print("\t) \033[36m"+next(iter(action.keys()))+"\033[0m")
    print("\033[33m"+("_"*width)+"\n\033[0m", end="\r\033[A")
    print("\033[A\t> ", end='\r')
    print("\033[31m", end="")
    print_top_right("No device connected")
    print("\033[0m", end="")
    print_top_left("idle")
    print("\033[?25l", end="")
    while running: sleep(1)
    print("\033[?25h\n")