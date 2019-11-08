from pico2d import *
import random
import math
import time
from project.game_code.state_code import first_main_state
from project.game_code.object_code import game_world
from project.game_code.object_code.bottle import Bottle
from project.game_code.state_code import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 15.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

pi = 3.14159256
dragon_x = 480
dragon_y = 200


class Drunk:
    def __init__(self, x=dragon_x, y=dragon_y):
        self.x, self.y = x, y
        self.frame = 0
        self.dir = 1
        self.velocity = RUN_SPEED_PPS
        self.phase = 1
        self.is_hit = False
        self.image = load_image('sprite\\Enemy\\boss.png')
        self.hp = 200
        self.bottle_number = 0
        self.attack_timer = 0
        self.radius = 2
        self.angle = 0
        self.speed_control = 0
        self.y_direction = 1
        self.check_attack_start_time = time.time()
        self.check_attack_end_time = 0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.check_attack_end_time = time.time() - self.check_attack_start_time

        if self.hp >= 150:
            self.phase = 1
        elif self.hp >= 60:
            self.phase = 2
        else:
            self.phase = 3

        if self.check_attack_end_time > (1 - (self.phase * 0.1)):
            self.bottle()
            self.bottle_number = (self.bottle_number + 1) % 16
            self.check_attack_start_time = time.time()

        if self.phase == 1:
            if self.dir == 1:
                self.x += self.velocity * game_framework.frame_time
                if self.x >= 660:
                    self.dir = -1
            else:
                self.x -= self.velocity * game_framework.frame_time
                if self.x <= 300:
                    self.dir = 1

        elif self.phase == 2:
            self.angle += 1
            self.angle = self.angle % 360
            self.x += self.radius * math.cos(self.angle * pi / 180)
            self.y += self.radius * math.sin(self.angle * pi / 180)
            if 90 <= self.angle <= 270:
                self.dir = -1
            else:
                self.dir = 1

        else:
            if self.dir == 1:
                self.x += self.velocity * game_framework.frame_time
                if self.x >= 870:
                    self.dir = -1
            else:
                self.x -= self.velocity * game_framework.frame_time
                if self.x <= 90:
                    self.dir = 1

            if self.y_direction == 1:
                self.y += self.velocity * game_framework.frame_time
                if self.y >= 470:
                    self.y_direction = -1
            else:
                self.y -= self.velocity * game_framework.frame_time
                if self.y <= 90:
                    self.y_direction = 1

    def draw(self):
        if self.phase == 3:
            if self.dir > 0:
                self.image.clip_draw(int(self.frame) * 64, 384, 64, 64, self.x, self.y, 200, 200)
            else:
                self.image.clip_draw(int(self.frame) * 64, 448, 64, 64, self.x, self.y, 200, 200)

        else:
            if self.dir > 0:
                self.image.clip_draw(int(self.frame) * 64, 512, 64, 64, self.x, self.y, 200, 200)
            else:
                self.image.clip_draw(int(self.frame) * 64, 576, 64, 64, self.x, self.y, 200, 200)

    def bottle(self):
        bottle = Bottle(self.x, self.y, self.phase, self.bottle_number)
        game_world.add_object(bottle, 1)
