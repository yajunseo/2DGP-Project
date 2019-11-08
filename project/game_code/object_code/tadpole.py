from pico2d import *
import random
import time
from project.game_code.state_code import second_main_state
from project.game_code.object_code import game_world
from project.game_code.state_code import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4


class Tadpole:
    image = None

    def __init__(self, x, y, direction):
        self.x, self.y = x, y
        self.turn = 0
        self.frame = random.randint(0, 12)
        self.dir = direction
        self.velocity = RUN_SPEED_PPS
        self.is_hit = False
        self.check_start_time = time.time()
        self.check_turn_time = 0
        if self.image is None:
            self.image = load_image('sprite\\Enemy\\tadpole.png')

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12
        self.check_turn_time = time.time() - self.check_start_time

        if self.dir == 1:
            if self.check_turn_time < 0.8:
                self.x += self.velocity * game_framework.frame_time
            else:
                self.dir = -1
                self.turn = 0
                self.check_start_time = time.time()

        else:
            if self.check_turn_time < 0.8:
                self.x -= self.velocity * game_framework.frame_time
            else:
                self.dir = 1
                self.turn = 0
                self.check_start_time = time.time()
        self.x = clamp(70, self.x, 960 - 70)

    def draw(self):
        if self.is_hit:
            self.image.clip_draw(int(self.frame) * 16, 96, 16, 16, self.x, self.y, 50, 50)

        else:
            if self.dir == 1:
                self.image.clip_draw(int(self.frame) * 16, 224, 16, 16, self.x, self.y, 50, 50)
            else:
                self.image.clip_draw(int(self.frame) * 16, 240, 16, 16, self.x, self.y, 50, 50)
