#This is the main runner script
#plan with this software is to be run in different configured modes, the type of adb integration will be defined here.
#it can also be run through termux to have a whole on device setup, the install proceedure goes as follows on Arch Linux

# +---------+------------------------------+
# | Step #1 | sudo pacman -S python        |
# | Step #2 | pip install pypresense       |
# | Step #3 | sudo pacman -S android-tools |
# | Step #4 | configure your device        |
# | Step #5 | python run.py                |
# +---------+------------------------------+

import rpc

if __name__ == "__main__":
    print("Reading config...", end='\r')
    print("Connecting to device...", end='\r')
    print("Connecting to Discord...", end='\r')
    rpc.connect()
    
    input("Press return when Arcaea is running...")
    print("\033[FRunning main loop                     ")