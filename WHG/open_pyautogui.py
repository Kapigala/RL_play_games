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
import mss
import keyboard
from pyscreeze import locateAll,locate

#game_path=r"C:\Users\Kacper\PycharmProjects\RL_play_games\WHG\game_source\the-worlds-hardest-game.exe"
game_path=r"C:\Users\Kacper\PycharmProjects\RL_play_games\WHG\game_source\WHGTrainer.exe"

p = subprocess.Popen(game_path,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,)
#time.sleep(1.5) #old pc setup
time.sleep(1.3)

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

monitor = {"top": luc[1]+25, "left": luc[0], "width": int(rdc[0]-luc[0]), "height": int(rdc[1]-25-luc[1]-25)}

ys = ImageOps.grayscale(Image.open('yellow_square2.png'))
coin = ImageOps.grayscale(Image.open('coin_color.png'))


while p.poll() is None: #Start loop
    move_time = time.time()

    sc = mss.mss().grab(monitor)
    pic = ImageOps.grayscale(Image.frombytes("RGB", sc.size, sc.bgra, "raw", "BGRX"))
    time.sleep(0.001)
    #coins_now
    print("CURRENT STATE:",coins_now,delta_reward,t)

    move = random.choice([
                            ["left"],["up"],["right"],["down"],
                            [],["down","left"],["down","left"],["up","right"],["up","left"]
                            ])
    print("Action",move)

    for m in move:
        keyboard.press(m)
    time.sleep(0.1)
    for m in move:
        keyboard.release(m)

    if pic.getpixel((1,30)) == 220:
        delta_reward +=  1000
        print(f"attempt {live} wins - score:{delta_reward}")
        ys = ImageOps.grayscale(Image.open('yellow_square_new.png')) #NOT SURE WHY THIS CHANGE IN TRAINING GAME
        #DURING PRETREIN
        #p.kill()
        lvl += 1
        try:
            os.mkdir(fr"../WHG/Train_sessions/{session}/lvl_{lvl}")
        except:
            pass

        time.sleep(5)
        try:
            coins_now=len(list(py.locateAllOnScreen('coin_color.png',confidence=0.8,region=(luc[0], luc[1], rdc[0], rdc[1]))))
        except:
            coins_now = 0

        #next lvl init TODO:
        #-current coint
        #-new full_sc

    print(locate(ys, pic))
    if locate(ys, pic,grayscale=True) != None:
        delta_reward -= 1
        if coins_now != 0:
            bon = coins_now
            #coins_now = len(list(py.locateAllOnScreen('coin_color.png', confidence=0.8,region=(luc[0], luc[1], rdc[0], rdc[1]))))
            coins_now = len(list(locateAll(coin,pic)))
            delta_reward += 10*(bon-coins_now)
    else:
        if pic.getpixel((1,30)) == 220:
            continue
        print("DEATH ON FRAME",t-1) #
        #pic.show()
        delta_reward -= 100
        print(f"attempt {live} fails - score:{delta_reward}")
        # zapisz jako wynik sesji t
        #UZWGLĘDNIJ ZE T-1 FAILOWAŁO //zmodyfikować
        time.sleep(0.2)
        #try:
         #   coins_now = len(
          #      list(py.locateAllOnScreen('coin_color.png', confidence=0.8
                                     #     , region=(luc[0], luc[1], rdc[0], rdc[1]))))
           # print("COIN BACK",coins_now)
        #except:
         #   coins_now = 0
        coins_now = len(list(py.locateAllOnScreen('coin_color.png', confidence=0.8
                                              , region=(luc[0], luc[1], rdc[0], rdc[1]))))
        print("COIN NOW:",coins_now)
        live += 1
        t=0

    pic.save(fr"../WHG/Train_sessions/{session}/lvl_{lvl}/{live}_{t}.png")
    t += 1

    #terminations
    if t==200:
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