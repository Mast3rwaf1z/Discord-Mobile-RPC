#This is the main runner script
#plan with this software is to be run in different configured modes, the type of adb integration will be defined here.
#the install proceedure goes as follows on Arch Linux

# +---------+------------------------------+
# | Step #1 | sudo pacman -S python        |
# | Step #2 | pip install pypresense       |
# | Step #3 | sudo pacman -S android-tools |
# | Step #4 | configure your device        |
# | Step #5 | python run.py                |
# +---------+------------------------------+

import os
import time

import Discord
import Arcaea
import ProjectSekai
import Config

config:dict = None

def getGame():
    game = None
    while game is None:
        status = os.popen("adb shell dumpsys window | grep mCurrentFocus").read()
        match status.split("u0 ")[1].split("/")[0]:
            case Arcaea.Arcaea.name:
                game = Arcaea.Arcaea()
                break
            case ProjectSekai.ProjectSekai.name:
                game = ProjectSekai.ProjectSekai()
                break
        time.sleep(1)
    
    return game

def connectADB():
    response = ""
    if config["connection_type"] == "wireless":
        response = os.popen(f'adb connect {config["ip"]}:{config["port"]}')
    if response == f'connected to {config["ip"]}:{config["port"]}':
        print("successfully connected to wireless device!               ", end="\r")


if __name__ == "__main__":
    print("Reading config...                                                ", end='\r')
    config = Config.read()
    print("Connecting to device...                                          ", end='\r')
    connectADB()

    while True:
        print("Select a game...                                              ", end='\r')
        game = getGame()
        print("Connecting to Discord...                                         ", end='\r')
        Discord.connect(game.id)

        print("Running main loop                                                ", end='\r')
        Discord.main(game)