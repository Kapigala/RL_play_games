import subprocess
import pyautogui as py
from time import time,sleep
import numpy as np
import random
import sys
from datetime import date
import os
from PIL import Image, ImageOps
import mss
import keyboard
from pyscreeze import locateAll,locate

#game_path=r"C:\Users\Kacper\PycharmProjects\RL_play_games\WHG\game_source\the-worlds-hardest-game.exe"
game_path=r"C:\Users\Kacper\PycharmProjects\RL_play_games\WHG\game_source\WHGTrainer.exe"

p = subprocess.Popen(game_path,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,)
#sleep(1.5) #old pc setup
sleep(1.3)

s_location = py.locateOnScreen('game_finder.png')
x,y = py.center(s_location)

luc, rdc = (x-274,y-166),(x+272,y+230)

py.click((x,y))

production=False

if production:
    sleep(2.7)
    for i in range(8):
        if p.poll() is None:
            sleep(1.1)
    if p.poll() is None:
        py.click(x=x-217, y=y+96)
        sleep(1)
    else:
        sys.exit()

    if p.poll() is None:
        py.moveTo((x+82,y+143))
        py.click()
        sleep(1.5)
    else:
        sys.exit()

else:
    sleep(1)
    if p.poll() is None:
        py.click(x=x-115, y=y+96)
        sleep(0.3)
        py.click(x=x - 115, y=y + 96)
    else:
        sys.exit()

    if p.poll() is None:
        py.moveTo((x+82,y+143))
        py.click()
        sleep(1.5)
    else:
        sys.exit()

t=0
#session start live = 0
live=1
session = str(date.today()).replace("-","_")
lvl=1

try:
    os.mkdir(fr"../WHG/Train_sessions/{session}")
except:
    pass

try:
    os.mkdir(fr"../WHG/Train_sessions/{session}/lvl_1")
    os.mkdir(fr"../WHG/Train_sessions/{session}/raport_1")
except:
    pass


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

if not os.path.isfile(fr"../WHG/Train_sessions/{session}/raport_{lvl}/reward_track.txt"):
    f = open(fr"../WHG/Train_sessions/{session}/raport_{lvl}/reward_track.txt", "w")
    f.write("live,time_step,action,reward,sigle_reward\n")
else:
    f = open(fr"../WHG/Train_sessions/{session}/raport_{lvl}/reward_track.txt", "a")

while p.poll() is None: #Start loop
    move_time = time()

    sc = mss.mss().grab(monitor)
    pic = ImageOps.grayscale(Image.frombytes("RGB", sc.size, sc.bgra, "raw", "BGRX"))

    #print(np.array(pic).shape)
    #raise

    #coins_now
    print("CURRENT STATE:",coins_now,delta_reward,t)

    pic.save(fr"../WHG/Train_sessions/{session}/lvl_{lvl}/{live}_{t}.png") # pic before action

    move = random.choice([
                            ["left"],["up"],["right"],["down"],
                            [],["down","left"],["down","left"],["up","right"],["up","left"]
                            ])
    print("Action",move)

    #żółty == pixel 14

    #print(np.array(pic).shape)
    #for y in range(346): # V
     #   for x in range(546):
      #      if pic.getpixel((x,y))!=189:
       #         print(x,y,pic.getpixel((x,y)))
    #raise
    #if pic.getpixel((50,50))==94:
     #  pic.show()
      #  raise
    print(locate(ys,pic))
    #raise

    #move=[]
    for m in move:
        keyboard.press(m)
        sleep(0.1)
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
            os.mkdir(fr"../WHG/Train_sessions/{session}/raport_{lvl}")
        except:
            pass

        t=0
        delta_reward=0
        live=1
        sleep(1.5)
        sc = mss.mss().grab(monitor)
        pic = ImageOps.grayscale(Image.frombytes("RGB", sc.size, sc.bgra, "raw", "BGRX"))
        coins_now = max(0,len(list(locateAll(coin,pic,confidence=0.8))))
        continue

    if locate(ys, pic,grayscale=True,confidence=0.98) != None:
        delta_reward -= 1
        if coins_now != 0:
            bon = coins_now
            coins_now = len(list(locateAll(coin,pic,confidence=0.8)))
            delta_reward += 10*(bon-coins_now)
    else:
        if pic.getpixel((1,30)) == 220:
            continue
        delta_reward -= 100
        print(f"attempt {live} fails - score:{delta_reward}")
        # zapisz jako wynik sesji t
        #UZWGLĘDNIJ ZE T-1 FAILOWAŁO //zmodyfikować
        f.write(f"{live},{t-1},{move},{delta_reward},-100\n")
        sleep(1)
        coins_now = max(0,len(list(locateAll(coin,pic,confidence=0.8))))

        delta_reward = 0
        live += 1
        t=0
        continue

    t += 1

    #terminations
    if t==101: #per lvl-specified in the future
        delta_reward -= 50
        print(f"attempt {live} fails [run out of time] - score:{delta_reward}")
        # zapisz jako wynik sesji t
        py.keyDown("r")
        py.keyUp("r")
        sleep(0.2)
        coins_now = max(0,len(list(locateAll(coin,pic,confidence=0.8))))

        f.write(f"{live},{t-1},{move},{delta_reward},-1\n")
        delta_reward = 0
        live += 1
        t = 0

    else:
        f.write(f"{live},{t-1},{move},{delta_reward},-1\n")

    print("loop_time:",time()- move_time)
p.kill()
print("QUIT")