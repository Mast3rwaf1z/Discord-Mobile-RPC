# Discord Mobile RPC
Hi, this project is inspired by the fact that there isn't really a working lightweight solution to have mobile games running with RPC except having a samsung phone... The documentation of pypresence was pretty simple so i descided to make something of my own. This repo was also created as an answer to [this repository](https://github.com/chinosk6/Arcaea_Discord_Rich_Presence) being in chinese, although it does not have as many features.

# Requirements
This was developed on Arch Linux, here's a guide on how to get it running on any Arch Linux machine:
```zsh
sudo pacman -S python android-tools
pip install pypresence
```

# Installation
This is easy:

1. clone this repository, 
2. edit the config with the ip, port and connection method of your device if any (not required if your device is connected with a cable)
3. run `python run.py`

# Pull requests
If you wish to add more games to this repository, feel free to open a pull request, if more are added i might move the files to its own directory and load them automatically in the future. A new game should follow the example implementation in `Arcaea.py`, and be added to the switch in `run.py`.

# Example
<image src="https://cdn.discordapp.com/attachments/889964274229854248/1074850779233533952/image.png">
