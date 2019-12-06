from pico2d import *
import random
import math
import time
from project.game_code.state_code import first_main_state
from project.game_code.management_code import game_world
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


class Redpole:
    def __init__(self, x=dragon_x, y=dragon_y):
        self.x, self.y = x, y
        self.frame = 0
        self.dir = 1
        self.phase = 1
        self.image = load_image('sprite\\Enemy\\tadpole.png')
        self.hp = 21
        self.lightning_number = 0
        self.radius = 2
        self.angle = 0
        self.speed_control = 0
        self.y_direction = 1
        self.is_beaten = False
        self.is_dead = False
        self.is_lock = False
        self.check_attack_start_time = 0
        self.check_attack_end_time = 0
        self.check_second_attack_start_time = 0
        self.check_second_attack_end_time = 0
        self.check_dead_motion_start_time = 0
        self.check_dead_motion_end_time = 0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12
        self.check_attack_end_time = get_time() - self.check_attack_start_time
        self.check_second_attack_end_time = get_time() - self.check_second_attack_start_time
        if self.hp >= 18:
            self.phase = 1
        elif self.hp >= 6:
            self.phase = 2
        else:
            self.phase = 3

        if not self.is_lock:
            if self.phase == 1:
                if self.dir == 1:
                    self.x += RUN_SPEED_PPS * game_framework.frame_time
                    if self.x >= 660:
                        self.dir = -1
                else:
                    self.x -= RUN_SPEED_PPS * game_framework.frame_time
                    if self.x <= 300:
                        self.dir = 1

            elif self.phase == 2:
                if self.dir == 1:
                    self.x += RUN_SPEED_PPS * game_framework.frame_time
                    if self.x >= 870:
                        self.dir = -1
                else:
                    self.x -= RUN_SPEED_PPS * game_framework.frame_time
                    if self.x <= 90:
                        self.dir = 1

                if self.y_direction == 1:
                    self.y += RUN_SPEED_PPS * game_framework.frame_time
                    if self.y >= 470:
                        self.y_direction = -1
                else:
                    self.y -= RUN_SPEED_PPS * game_framework.frame_time
                    if self.y <= 90:
                        self.y_direction = 1

            else:
                if self.dir == 1:
                    self.x += RUN_SPEED_PPS * game_framework.frame_time
                    if self.x >= 870:
                        self.dir = -1
                else:
                    self.x -= RUN_SPEED_PPS * game_framework.frame_time
                    if self.x <= 90:
                        self.dir = 1

                if self.y_direction == 1:
                    self.y += RUN_SPEED_PPS * game_framework.frame_time
                    if self.y >= 470:
                        self.y_direction = -1
                else:
                    self.y -= RUN_SPEED_PPS * game_framework.frame_time
                    if self.y <= 90:
                        self.y_direction = 1

        else:
            if self.is_dead:
                self.check_dead_motion_end_time = get_time() - self.check_dead_motion_start_time

    def draw(self):
        if self.is_lock:
            if not self.is_dead:
                self.image.clip_draw(int(self.frame) * 16, 32, 16, 16, self.x, self.y, 200, 200)

            else:
                self.image.clip_draw(int(self.frame) * 16, 0, 16, 16, self.x, self.y, 200, 200)

        else:
            if self.phase == 3:
                if self.dir > 0:
                    self.image.clip_draw(int(self.frame) * 16, 192, 16, 16, self.x, self.y, 200, 200)
                else:
                    self.image.clip_draw(int(self.frame) * 16, 208, 16, 16, self.x, self.y, 200, 200)

            else:
                if self.dir > 0:
                    self.image.clip_draw(int(self.frame) * 16, 160, 16, 16, self.x, self.y, 200, 200)
                else:
                    self.image.clip_draw(int(self.frame) * 16, 176, 16, 16, self.x, self.y, 200, 200)

    def bottle(self):
        bottle = Bottle(self.x, self.y, self.phase, self.bottle_number)
        game_world.add_object(bottle, 1)

    def get_bb(self):
        return self.x - 100, self.y - 100, self.x + 100, self.y + 100

