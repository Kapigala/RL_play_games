import subprocess
import pyautogui as py #Import pyautogui
import time #Import Time
import numpy as np
import random
import sys
import pyscreenshot

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
pic.show()

#p.kill()
#raise

for i in range(8):
    if p.poll() is None:
        time.sleep(1.1)
py.click(x=x-217, y=y+96)
time.sleep(1)
if p.poll() is None:
    sys.quit()
#py.click(x=x+82, y=y+143)
py.moveTo((x+82,y+143))
py.click()
time.sleep(1.5)

t=0

while p.poll() is None and t != 1000: #Start loop

    pic = pyscreenshot.grab(bbox=(luc[0], luc[1], rdc[0], rdc[1]))
    pic.show()

    #pic.save("WHG/Train_sessions/ss.png")

    move = random.choice(["a","w","s","d"])

    #py.press("d")
    py.keyDown(move)
    py.keyUp(move)
    #time.sleep(1)
    t += 1
p.kill()
print("QUIT")