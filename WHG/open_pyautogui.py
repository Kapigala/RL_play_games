import subprocess
game_path=r"C:\Users\Kacper\PycharmProjects\RL_play_games\WHG\game_source\the-worlds-hardest-game.exe"
#for i in range(N): #instances work

#TODO: NO SCREEN READ -SET WINDOW COORD
p = subprocess.Popen(game_path)
import pyautogui as py #Import pyautogui
import time #Import Time
time.sleep(2)

s_location = py.locateOnScreen('game_finder.png')
x,y = py.center(s_location)

print("//",(x,y))
#raise
py.click((x,y))
#raise

for i in range(8):
    if p.poll() is None:
        time.sleep(1.1)
py.click(x=x-217, y=y+96)
time.sleep(2)
#py.click(x=x+82, y=y+143)
py.moveTo((x+82,y+143))
py.click()
time.sleep(1.5)

t=0
while p.poll() is None and t != 5: #Start loop
    print (py.position())
    time.sleep(1)
    t += 1
p.kill()
print("QUIT")