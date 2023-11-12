from pyboy import PyBoy,WindowEvent

rom_path = r'../Mega_Man_V.gb'
pyboy = PyBoy(rom_path)

menu_state = open(r"C:\Users\Kacper\PycharmProjects\RL_play_games\Megaman_AI\states\game_start.state", "rb")
game_state = open(r"C:\Users\Kacper\PycharmProjects\RL_play_games\Megaman_AI\states\init_start.state", "rb")

pyboy.load_state(menu_state)
for i in range(100):
    pyboy.tick()

pyboy.load_state(game_state)


while not pyboy.tick():

    pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
    pyboy.tick()
    pyboy.tick()
    pyboy.tick()
    pyboy.tick()
    pyboy.tick()
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)
    pyboy.tick()
    pyboy.tick()
    pyboy.tick()
    pyboy.tick()
    pyboy.tick()
    pyboy.tick()
    pyboy.tick()
    pyboy.tick()
    pyboy.tick()
    pyboy.tick()
    pyboy.tick()
    pyboy.tick()
    pyboy.tick()
    pyboy.tick()
    pyboy.tick()
    pyboy.tick()
    pyboy.tick()
    print(pyboy.get_memory_value(0x0029))
    print(pyboy.get_memory_value(0x0026))
    #im = pyboy.screen_image()
    #pyboy.save_state()
    pyboy.stop()
#im.show()
#im.save("start_screen.jpg")
