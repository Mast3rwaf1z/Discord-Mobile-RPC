import pypresence
import Game
import time

presence:pypresence.Presence = None

def connect(id):
    global presence
    presence = pypresence.Presence(client_id=id)
    presence.connect()


def main(game:Game):
    global presence
    start = time.time()
    while True:
        state = game.updatePresence(presence, start)
        if state == "idle": 
            presence.close()
            return
        time.sleep(15)