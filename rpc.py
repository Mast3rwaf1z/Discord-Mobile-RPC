import pypresence

def connect():
    presence = pypresence.Presence(client_id="1074775173749821510")
    presence.connect()
    presence.update(state="test", large_image="arcaea", details="test", large_text="test", small_image="test", small_text="test", )