import numpy as np
#import gymnasium as gym
#from gymnasium import spaces

import gym
from gym import spaces

import pyautogui as py
from PIL import Image, ImageOps,ImageGrab,ImageChops
import mss


class WHG_RL(gym.Env):
    """
    Custom Environment that follows gym interface.
    This is a simple env where the agent must learn to go always left.
    """

    def __init__(self,luc, rdc,grid_size=10,):
        super(WHG_RL, self).__init__()

        ys = ImageOps.grayscale(Image.open('yellow_square2.png'))
        coin = ImageOps.grayscale(Image.open('coin_color.png'))

        n_actions = 9
        self.action_space = spaces.Discrete(n_actions)
        # The observation will be the coordinate of the agent
        # this can be described both by Discrete and Box space
        self.observation_space = spaces.Box(low=0, high=255,
                                            shape=(1, 346, 546), dtype=np.uint8)
        self.luc=luc
        self.rdc=rdc
        self.monitor = {"top": luc[1]+25, "left": luc[0], "width": int(rdc[0]-luc[0]), "height": int(rdc[1]-25-luc[1]-25)}
        try:
            self.coins_now=len(list(py.locateAllOnScreen('coin_color.png',confidence=0.8)))
        except:
            self.coins_now = 0

    def reset(self):
        """
        Important: the observation must be a numpy array
        :return: (np.array)
        """
        py.keyDown("r")
        py.keyUp("r")
        try:
            self.coins_now = len(list(py.locateAllOnScreen('coin_color.png', confidence=0.8, region=(self.luc[0], self.luc[1], self.rdc[0], self.rdc[1]))))
        except:
            self.coins_now = 0

        sc = mss.mss().grab(self.monitor)
        pic = ImageOps.grayscale(Image.frombytes("RGB", sc.size, sc.bgra, "raw", "BGRX"))

        return pic, self.coins_now

    def step(self, action):
        if action == self.LEFT:
            self.agent_pos -= 1
        elif action == self.RIGHT:
            self.agent_pos += 1
        else:
            raise ValueError("Received invalid action={} which is not part of the action space".format(action))

        # Account for the boundaries of the grid
        self.agent_pos = np.clip(self.agent_pos, 0, self.grid_size)

        # Are we at the left of the grid?
        done = bool(self.agent_pos == 0)

        # Null reward everywhere except when reaching the goal (left of the grid)
        reward = 1 if self.agent_pos == 0 else 0

        # Optionally we can pass additional info, we are not using that for now
        info = {}

        return np.array([self.agent_pos]).astype(np.float32), reward, done, info

    def render(self, mode='console'):
        if mode != 'console':
            raise NotImplementedError()
        # agent is represented as a cross, rest as a dot
        print("." * self.agent_pos, end="")
        print("x", end="")
        print("." * (self.grid_size - self.agent_pos))

    def close(self):
        pass

#from stable_baselines3 import A2C

#from stable_baselines3.common.env_checker import check_env


#env = GoLeftEnv()

#env = GoLeftEnv(grid_size=10)

#obs = env.reset()
#env.render()

#print(env.observation_space)
#print(env.action_space)
#print(env.action_space.sample())

#GO_LEFT = 0
# Hardcoded best agent: always go left!
#n_steps = 20
#for step in range(n_steps):
 #   print("Step {}".format(step + 1))
  #  obs, reward, done, info = env.step(GO_LEFT)
   # print('obs=', obs, 'reward=', reward, 'done=', done)
    #env.render()
    #if done:
     #   print("Goal reached!", "reward=", reward)
      #  break