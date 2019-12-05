from pico2d import *
import time
import random
from math import sin, cos
from project.game_code.management_code import game_world
from project.game_code.state_code import game_framework


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

pi = 3.14159256


class Lightning:
    image = None

    def __init__(self, x, y, phase, number):
        self.x, self.y, self.phase, self.dir = x, y, phase, number * 22.5
        self.frame = 0
        self.lightning_color = random.randint(1, 2)
        self.velocity = 0.5 * phase

        if Lightning.image is None:
            Lightning.image = load_image('sprite\\Effect\\thunderEffect.png')

    def draw(self):
 #       draw_rectangle(*self.get_bb())
        if self.lightning_color == 1:
            self.image.clip_draw(0, int(self.frame) * 16, 16, 16, self.x, self.y, 50, 50)
        else:
            self.image.clip_draw(32, int(self.frame) * 16, 16, 16, self.x, self.y, 50, 50)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

        self.x += math.sin(self.dir * pi / 180)
        self.y += math.cos(self.dir * pi / 180)


    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

