from pyboy import PyBoy,WindowEvent
import PIL
import matplotlib.pyplot as plt
rom_path = r'C:\Users\Kacper\PycharmProjects\Pyboy_games\Mega_Man_V.gb'
pyboy = PyBoy(rom_path)
t=0
#state = open("game_start.state", "wb")
menu_state = open("game_start.state", "rb")
pyboy.load_state(menu_state)
game_state = open("init_start.state", "wb")
while not pyboy.tick():

    pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)
    pyboy.tick()

    t+=1
    print(t)
    if t==850:
        pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)
        pyboy.tick()
        pyboy.tick()
        pyboy.tick()
        pyboy.tick()
        pyboy.tick()
        pyboy.tick()
        pyboy.tick()
        im = pyboy.screen_image()
        pyboy.save_state(game_state)
        pyboy.stop()
im.show()
im.save("start_screen.jpg")
