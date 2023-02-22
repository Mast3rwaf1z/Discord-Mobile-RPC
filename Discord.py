import asyncio
import pypresence
import Game
import time

presence:pypresence.Presence = None

def connect(id):
    global presence
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    presence = pypresence.Presence(client_id=id)
    presence.connect()


def main(game:Game):
    global presence
    if presence is None: connect(game.id)
    start = time.time()
    while True:
        state = game.updatePresence(presence, start)
        if state == "idle": 
            presence.close()
            return
        time.sleep(15)