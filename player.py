import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
import vlc

def playSong(URL):
    vlcInstance = vlc.Instance()
    player = vlcInstance.media_player_new()
    player.set_mrl(URL)
    player.play()
    while True:
        pass
()