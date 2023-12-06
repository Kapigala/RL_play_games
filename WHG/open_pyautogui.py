import subprocess
import pyautogui as py #Import pyautogui
import time #Import Time
import numpy as np
import random
import sys
import pyscreenshot
from datetime import date
import os

game_path=r"C:\Users\Kacper\PycharmProjects\RL_play_games\WHG\game_source\the-worlds-hardest-game.exe"
#for i in range(N): #instances work

p = subprocess.Popen(game_path,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,)
time.sleep(1.2)


s_location = py.locateOnScreen('game_finder.png')
x,y = py.center(s_location)
#print(x,y)

luc, rdc = (x-274,y-166),(x+272,y+230)

#while True:
 #   print(py.position())
  #  print(x,y)

py.click((x,y))
#raise

time.sleep(2.7)

pic = pyscreenshot.grab(bbox=(luc[0], luc[1], rdc[0], rdc[1]))
pic.save("thumb_1.png")
#pic.show()

#p.kill()
#raise

for i in range(8):
    if p.poll() is None:
        time.sleep(1.1)
if p.poll() is None:
    py.click(x=x-217, y=y+96)
    time.sleep(1)
else:
    sys.exit()

if p.poll() is None:
    py.moveTo((x+82,y+143))
    py.click()
    time.sleep(1.5)
else:
    sys.exit()


t=0

#session start live = 0
live=1
session = str(date.today()).replace("-","_")
os.mkdir(fr"../WHG/Train_sessions/{session}")
while p.poll() is None and t != 10: #Start loop

    pic = pyscreenshot.grab(bbox=(luc[0], luc[1], rdc[0], rdc[1]))
    #pic.show()

    pic.save(fr"../WHG/Train_sessions/{session}/{live}_{t}.png")

    move = random.choice(["a","w","s","d"])
    py.keyDown(move)
    py.keyUp(move)
    t += 1
p.kill()
print("QUIT")