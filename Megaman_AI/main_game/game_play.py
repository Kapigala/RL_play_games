from pyboy import PyBoy,WindowEvent

rom_path = r'../Mega_Man_V.gb'
pyboy = PyBoy(rom_path)

menu_state = open(r"C:\Users\Kacper\PycharmProjects\RL_play_games\Megaman_AI\states\game_start.state", "rb")
game_state = open(r"C:\Users\Kacper\PycharmProjects\RL_play_games\Megaman_AI\states\init_start.state", "rb")

pyboy.load_state(menu_state)
for i in range(80):
    pyboy.tick()

pyboy.load_state(game_state)

ll="""$0014 to $---- = Keys pressed on pad 1
    $0015 to $---- = Always cleared
    $0016 to $---- = Keys held on pad 1
    $0017 to $---- = Always cleared
    $0018 to $---- = Palette changed
    $0019 to $---- = Draw horizontal data
    $001A to $---- = Draw vertical data
    $001B to $---- = Palette cycle stopped
    $001C to $---- = Update tile
    $001E to $---- = New tile position
    $0023 to $---- = New tile number
    $0026 to $---- = Current level
    $0027 to $---- = PRG bank for level
    $0028 to $---- = Scrolling direction
    $0029 to $---- = Area number
    $002A to $---- = Maximum screen
    $002B to $---- = Current screen
    $002C to $---- = Mirroring
    $002D to $---- = Life bar select
    $002E to $---- = Weapon bar select
    $002F to $---- = Boss bar enable
    $0030 to $---- = Current move
    $0031 to $---- = Direction
    $0032 to $---- = Current weapon
    $0033 to $---- = Shooting timer
    $0034 to $---- = Shooting flag
    $0035 to $---- = Sliding timer
    $0036 to $---- = Kill block type
        F0     => Kill
        00    => Nothing
        others => decrease life by 1
    $0037 to $---- = Platform sprite index
    $0038 to $---- = Charge counter
    $0039 to $---- = Platform direction
    $003A to $---- = Platform X speed low
    $003B to $---- = Platform X speed high
    $003C to $---- = Previous X pos low
    $003D to $---- = Previous X pos high
    $003E to $---- = Previous Y pos low
    $003F to $---- = Previous Y pos high
    #$0041 to $---- = Unused
    $0042 to $---- = Largest block type found
    $0043 to $---- = Nb. of destroyed blocks
    $0044 to $---- = Previous scroll X
    $0045 to $---- = Previous scroll Y
    $0046 to $---- = Vertical level
    $0047 to $---- = Block number to draw
    $0048 to $004F Block types in each tested position
    $0050 to $---- = Weapon selection in menu order
    #$0051 to $---- = Unused
    $0054 to $---- = Freeze counter
    $0055 to $---- = Horizontal autoscroll lock
    $0056 to $---- = Boss sprite index
    $0057 to $---- = Bump timer
    $0058 to $---- = Bump flag
    $0059 to $---- = Destroyed block disable
    $005A to $---- = Animation disable
    $005B to $---- = Shot type
    $005D to $---- = Picked up M-tank
    $0060 to $---- = Display updated
    $0069 to $---- = Last screen visited
    $006A to $---- = Current boss in rematch
    $006B to $---- = Killed bosses in rematch
    $006C to $---- = Current Wily level
    $006D to $---- = Beat letters
    $006E to $---- = Levels cleared
    $0074 to $---- = Show elevator borders
    $0075 to $---- = Elevator position low
    $0076 to $---- = Elevator position high
    $0078 to $---- = Split parameters
    $0080 to $008F = Thread info
    $0090 to $---- = VBL flag
    $0092 to $---- = Asynchronous frame counter
    $0093 to $0094 Execute address
    $0095 to $---- = Critical section flag
    $0096 to $---- = Split effect enabled
    $0097 to $0098 Split effect execution routine
    $0099 to $---- = Next split effect number
    $009A to $---- = Current split effect number
    $009B to $---- = Next split position
    $009C to $---- = Current split position
    $009D to $---- = Synchronous frame counter
    $009E to $---- = Current sprite drawn
    $009F to $---- = Next OAM table offset
    $00A0 to $---- = Freeze frame
    $00A1 to $---- = Gravity
    $00A2 to $---- = Current Y scroll
    $00A4 to $---- = Current X scroll
    $00A5 to $---- = Current name table
    $00A6 to $---- = Current sprite
    $00A7 to $---- = Saved X register when PRG change interrupted
    $00A8 to $---- = Saved Y register when PRG change interrupted
    $00A9 to $---- = Colour lock
    $00AC to $---- = Horizontal scroll direction
    $00AD to $---- = Next enemy in level
    $00AE to $---- = Previous enemy in level
    $00AF to $---- = Mega man upside down
    $00B0 to $---- = Life
    $00B1 to $00BC = Weapon energy
    $00BD to $---- = E-tanks
    $00BE to $---- = M-tanks
    $00BF to $---- = Lives
    $00C0 to $---- = In sound code
    $00C7 to $---- = Song time increment
    $00C8 to $---- = Song time low
    $00C9 to $---- = Song speed high
    $00CA to $---- = Song spedd low
    $00CB to $---- = Global transpose
    $00CC to $---- = SF channels playing
    $00CF to $---- = Current track bit
    $00D0 to $00D1 = SF pointer
    $00D2 to $---- = SF transpose
    $00D3 to $---- = SF ontime
    $00D4 to $---- = SF timer
    $00D5 to $---- = SF on-timer
    $00DA to $---- = Sound queue write pointer
    $00DB to $---- = Sound queue read pointer
    $00DC to $00E3 = Sound queue
    $00E4 to $00E7 = LSFR
    $00E8 to $00E9 = NMI return address
    $00EA to $00EB = Background CHR banks
    $00EC to $00EF = Sprite CHR banks
    $00F0 to $---- = Screen disabled
    $00F2 to $---- = Last MMC3 command
    $00F3 to $---- = Last PRG bank 8000 to 9FFF
    $00F4 to $---- = Last PRG bank A000 to BFFF
    $00F5 to $---- = New PRG bank 8000 to 9FFF
    $00F6 to $---- = New PRG bank A000 to BFFF
    $00F7 to $---- = In PRG change
    $00F8 to $---- = Postponed PRG change
    $00F9 to $---- = Scroll X high
    $00FA to $---- = Scroll Y
    $00FB to $---- = Vertical screen offset
    $00FC to $---- = Scroll X
    $00FD to $---- = Current nametable
    $00FE to $---- = Display settings 1
    $00FF to $---- = Display settings 2
    $0100 to $011F = Powerups taken in level
    $0150 to $016F = Debug stack
    $0170 to $017F = Main stack
    $0190 to $01AF = Palette animation stack
    $01B0 to $01DF = Game stack
    $01E0 to $01FF = System stack
    $0200 to $02FF = OAM table
    $0300 to $0317 = Sprite type
    $0318 to $032F = X position fraction
    $0330 to $0347 = X position low
    $0348 to $035F = X position high
    $0360 to $0377 = Y position fraction
    $0378 to $038F = Y position low
    $0390 to $03A7 = Y position high
    $03A8 to $03BF = X speed low
    $03C0 to $03D7 = X speed high
    $03D8 to $03EF = Y speed low
    $03F0 to $0407 = Y speed high
    $0408 to $041F Sprite flags
        7       => Hurts Mega Man
        6       => Shielded,
        5 to  0 => Size
    $0420 to $0437 = Direction
    $0438 to $044F = Sprite number
    $0450 to $0467 = Life
    $0468 to $047F = Variable A
    $0480 to $0497 = Variable B
    $0498 to $04AF = Variable C
    $04B0 to $04C7 = Variable D
    $04C8 to $04DF = Variable E
    $04E0 to $04F7 = Variable F
    $04F8 to $050F = Variable G
    $0510 to $0527 = Variable H
    $0528 to $053F = Display flags
        6 => Flipped
        5 => Mirrored,
        4 => In  background
        3 => Don't destroy when off screen
        2 => Invisible
    $0540 to $0557 = Animation frame
    $0558 to $056F = Animation
    $0570 to $0587 = Animation timer
    $0588 to $059F = Enemy handler low
    $05A0 to $05B7 = Enemy handler high
    $05B8 to $05CF = Flash counter
    $05D0 Background animation
    $05D1 Background frame
    $05D2 Background timer
    $05E0 to $05EF = Current column
    $05F0 to $05F3 = Palette animation
    $05F4 to $05F7 = Palette frame
    $05F8 to $05FB = Palette timer
    $0600 to $061F = Palette
    $0620 to $063F = Original palette
    $0640 to $067F = Attribute table
    $0680 to $06BF = Local destroyed blocks
    $06C0 to $06FF = Destroyed blocks
    $0700 to $077F = Channel variables
    $0780 to $07FF = Drawing buffer"""

def summary(ll):
    print("--"*20)
    for el in ll.split("\n"):
        if el.lstrip()[0]=="$":
            if el.lstrip()[10]=="-":
                print(el.lstrip()[17:],"-",pyboy.get_memory_value(int(f"0x{el.lstrip()[1:5]}",16)))
            else:
                print(el.lstrip()[17:],"range_loop_needed - TODO")
        elif el.lstrip()[0]!="#":
            print(el.lstrip())
    print("--"*20)

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
    pyboy.tick()
    pyboy.tick()

    summary(ll)
    #im = pyboy.screen_image()
    #pyboy.save_state()
    pyboy.send_input(WindowEvent.PRESS_ARROW_LEFT)
    pyboy.tick()
    pyboy.tick()
    pyboy.tick()
    pyboy.tick()
    pyboy.tick()
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_ARROW_LEFT)
    pyboy.tick()
    pyboy.tick()
    summary(ll)
    #pyboy.stop()

    pyboy.send_input(WindowEvent.PRESS_BUTTON_B)
    pyboy.tick()
    summary(ll)
    pyboy.tick()
    pyboy.tick()
    pyboy.tick()
    pyboy.tick()
    pyboy.stop()
#im.show()
#im.save("start_screen.jpg")
