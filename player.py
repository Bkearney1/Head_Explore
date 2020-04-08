import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
import vlc
import time

vlcInstance = vlc.Instance()
player = vlcInstance.media_player_new()
play_flag = 1


def test_loop():
    while True:
        print("testing")
()

def playSong(URL):
        i=0
        player.set_mrl(URL)
        player.play()
()

#294.566 == 4MIN 54SEC
#this is kinda weird stuff... trying to figure out a good way to get autoplay working


def nextSong():
    print("next song,please")
    print(player.get_state())
def stopall():
    time.sleep(.5)
    player.stop()

    ()
def pause():
    time.sleep(.25)
    player.pause()