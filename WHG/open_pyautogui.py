import subprocess
import pyautogui as py #Import pyautogui
import time #Import Time
import numpy as np
import random
import sys
import pyscreenshot
from datetime import date
import os
from PIL import Image, ImageOps,ImageGrab,ImageChops
import cv2

#game_path=r"C:\Users\Kacper\PycharmProjects\RL_play_games\WHG\game_source\the-worlds-hardest-game.exe"
game_path=r"C:\Users\Kacper\PycharmProjects\RL_play_games\WHG\game_source\WHGTrainer.exe"

p = subprocess.Popen(game_path,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,)
#time.sleep(1.5) #old pc setup
time.sleep(1.2)

s_location = py.locateOnScreen('game_finder.png')
x,y = py.center(s_location)

luc, rdc = (x-274,y-166),(x+272,y+230)

#py.click(luc)
#time.sleep(3)

py.click((x,y))

production=False

if production:
    time.sleep(2.7)
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

else:
    time.sleep(1)
    if p.poll() is None:
        py.click(x=x-115, y=y+96)
        time.sleep(0.3)
        py.click(x=x - 115, y=y + 96)
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
try:
    os.mkdir(fr"../WHG/Train_sessions/{session}")
except:
    pass

try:
    os.mkdir(fr"../WHG/Train_sessions/{session}/lvl_1")
except:
    pass

lvl=1
# INIT controlers
print("TRAINING SESSION START")

delta_reward=0
try:
    coins_now=len(list(py.locateAllOnScreen('coin_color.png',confidence=0.8)))
except:
    coins_now = 0

while p.poll() is None: #Start loop
    move_time=time.time()
    pic = ImageOps.grayscale(pyscreenshot.grab(bbox=(luc[0], luc[1]+25, rdc[0], rdc[1]-25)))

    #coins_now
    print("CURRENT STATE:",coins_now,delta_reward,t)

    #if train
    pic.save(fr"../WHG/Train_sessions/{session}/lvl_{lvl}/{live}_{t}.png")

    move = random.choice([
                            ["left"],["up"],["right"],["down"],
                            [],["down","left"],["down","left"],["up","right"],["up","left"]
                            ])
    print("Action",move)

    py.FAILSAFE = False
    for m in move:
        py.keyDown(m)
    for m in move:
        py.keyUp(m)
    py.FAILSAFE = True

    t += 1

    if pic.getpixel((1,30)) == 220:
        delta_reward +=  1000
        print(f"attempt {live} wins - score:{delta_reward}")
        # zapisz jako wynik sesji t
        #ifwin = full_sc.crop((245,0,305,21))
        #time.sleep(0.1) #could be longer

        #DURING PRETREIN
        #p.kill()
        lvl += 1
        try:
            os.mkdir(fr"../WHG/Train_sessions/{session}/lvl_{lvl}")
        except:
            pass

        try:
            coins_now=len(list(py.locateAllOnScreen('coin_color.png',confidence=0.8)))
        except:
            coins_now = 0

        break
        time.sleep(1) #wait to go next
        coins_now = len(list(py.locateAllOnScreen('coin_color.png', confidence=0.8, region=(luc[0], luc[1], rdc[0], rdc[1]))))

        """
        #next lvl init TODO:
        -current coint
        -new full_sc
        """

    try:
        list(py.locateOnScreen('yellow_square.png', confidence=0.9, region=(luc[0], luc[1], rdc[0], rdc[1])))[0]
        delta_reward -= 1
        if coins_now != 0:
            bon = coins_now
            coins_now = len(list(py.locateAllOnScreen('coin_color.png', confidence=0.8,region=(luc[0], luc[1], rdc[0], rdc[1]))))
            delta_reward += 10*(bon-coins_now)
    except:
        delta_reward -= 100
        print(f"attempt {live} fails - score:{delta_reward}")
        # zapisz jako wynik sesji t
        time.sleep(0.1)
        try:
            coins_now = len(
                list(py.locateAllOnScreen('coin_color.png', confidence=0.8
                                          , region=(luc[0], luc[1], rdc[0], rdc[1]))))
        except:
            coins_now = 0
        live += 1
        t=0

    #terminations
    if t==20:
        delta_reward -= 50
        print(f"attempt {live} fails [run out of time] - score:{delta_reward}")
        # zapisz jako wynik sesji t
        #time.sleep(0.1)
        py.keyDown("r")
        py.keyUp("r")
        try:
            coins_now = len(list(py.locateAllOnScreen('coin_color.png', confidence=0.8, region=(luc[0], luc[1], rdc[0], rdc[1]))))
        except:
            coins_now = 0
        delta_reward = 0
        live += 1
        t = 0
    print("loop_time:",time.time()- move_time)
p.kill()
print("QUIT")