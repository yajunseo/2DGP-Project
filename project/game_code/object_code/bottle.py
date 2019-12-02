from pico2d import *
import time
from math import sin, cos
from project.game_code.management_code import game_world
from project.game_code.state_code import game_framework


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

pi = 3.14159256


class Bottle:
    image = None

    def __init__(self, x, y, phase, number):
        if Bottle.image is None:
            Bottle.image = load_image('sprite\\Effect\\bottle.png')
        self.x, self.y, self.phase, self.dir = x, y, phase, number * 22.5
        self.frame = 0
        self.velocity = 0.5 * phase

    def draw(self):
 #       draw_rectangle(*self.get_bb())
        self.image.clip_draw(int(self.frame) * 12 + 2, 0, 11, 14, self.x, self.y, 40, 40)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

        self.x += math.sin(self.dir * pi / 180)
        self.y += math.cos(self.dir * pi / 180)


    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

