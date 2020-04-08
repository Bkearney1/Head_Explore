import os
from threading import Timer
import threading
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
import vlc
import time
from webScraper import set_mp3s
vlcInstance = vlc.Instance()
player = vlcInstance.media_player_new()
play_flag = 1




def hello():
    print("hello there!")

def playSong(URL, startIndex):
        index = startIndex

        player.set_mrl(URL)
        player.play()
        print("playing index " + str(index))

        def CheckForEnd():
            done = False
            while not done:
                if(player.get_state() == vlc.State.Ended):
                    print("done")
                    if(index<len(set_mp3s)):        #make sure it doesnt crash at end of show
                        playSong(set_mp3s[index],index)
            #control of what is currently playing is passed from the GUI to this thread from this point on
        index+=1
        thread = threading.Thread(target=CheckForEnd)
        thread.daemon = True
        thread.start()


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