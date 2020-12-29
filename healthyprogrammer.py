from pygame import mixer
from datetime import datetime
from time import time


def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == "__main__":
    # musiconloop("shona.mp3", "stop")
    init_water = time()
    init_eye = time()
    init_phy = time()
    watersecs = 5
    eyessecs = 10
    physecs = 20
    while True:
        if time() - init_water > watersecs:
            print("Water drinking time. Please enter 'drank' to stop the alarm")
            musiconloop("shona.mp3", 'drank')
            log_now("Water drank at")

        if time() - init_eye > eyessecs:
            print("Eyes Exercise time. Please enter 'doneeyes' to stop the alarm")
            musiconloop("eyes.mp3", 'doneeyes')
            log_now("Eyes Exercise done at")

        if time() - init_phy > physecs:
            print("Physical Exercise time. Please enter 'donephy' to stop the alarm")
            musiconloop("exercise.mp3", 'donephy')
            log_now("Physical Exercise at")        