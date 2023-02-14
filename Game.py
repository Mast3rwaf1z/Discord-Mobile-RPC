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
            details=f'{os.popen("adb devices -l | grep device").read().split("device:")[1].split(" ")[0]}', 
            state=self.getStatus(),
            large_image=self.image,
            start=int(startTime),
            buttons=[{"label":f"Get {self.displayName}", "url":self.url}]
        )
        return self.getStatus().lower()

