import os
import time
import pypresence

class Game:
    def __init__(self) -> None:
        response = ""
        while not self.name in response:
            response = os.popen("adb shell dumpsys window | grep mCurrentFocus").read()
            if self.name in response: break
            print(f"Please launch {self.displayName}...", end='\r')
            time.sleep(1)
    
    def getStatus(self):
        status = os.popen("adb shell dumpsys window | grep mCurrentFocus").read()
        if self.name in status:
            return f"Playing {self.displayName}"
        else:
            return "Idle"

    
    def updatePresence(self, presence:pypresence.Presence, startTime):
        presence.update(
            state=self.getStatus(), 
            large_image=self.image,
            start=int(startTime)
        )
        return self.getStatus().lower()

