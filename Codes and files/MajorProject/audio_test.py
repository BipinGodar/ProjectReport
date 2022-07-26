# Stop the Sound via multiprocessing
import multiprocessing
from playsound import playsound

p = multiprocessing.Process(target=playsound, args=("Hello.mp3",))
p.start()
input("press ENTER to stop playback")
p.terminate()