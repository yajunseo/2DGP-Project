from pico2d import *
import time
import random
from math import sin, cos
from project.game_code.management_code import game_world
from project.game_code.state_code import game_framework


class Turnip:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.number = 2
        self.spawn_start_time = 0
        self.spawn_check_time = 0
        self.is_spawn = False
        if Turnip.image is None:
            Turnip.image = load_image('sprite\\item\\moo.png')

    def draw(self):
 #       draw_rectangle(*self.get_bb())
        if self.is_spawn:
            self.image.draw(self.x, self.y, 40, 40)

    def update(self):
        self.spawn_check_time = get_time() - self.spawn_start_time

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

