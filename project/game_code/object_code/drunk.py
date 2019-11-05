from pico2d import *
import random
import math
from project.game_code.state_code import main_state
from project.game_code.object_code import game_world
from project.game_code.object_code.bottle import Bottle

pi = 3.14159256
dragon_x = 480
dragon_y = 200


class Drunk:
    def __init__(self, x=dragon_x, y=dragon_y):
        self.x, self.y = x, y
        self.frame = 0
        self.dir = 1
        self.frame_speed_control = 0
        self.phase = 3
        self.is_hit = False
        self.image = load_image('sprite\\Enemy\\boss.png')
        self.hp = 200
        self.bottle_number = 0
        self.attack_timer = 0
        self.radius = 2
        self.angle = 0
        self.speed_control = 0
        self.y_direction = 1

    def update(self):
        self.frame_speed_control += 1
        self.attack_timer += 1
        self.speed_control += 1
        if self.frame_speed_control > 50:
            self.frame = (self.frame + 1) % 8
            self.frame_speed_control = 0

        #        if self.hp >= 150:
        #            self.phase = 1
        #        elif self.hp >= 60:
        #            self.phase = 2
        #        else:
        #           self.phase = 3

        if self.attack_timer > 100 - (self.phase * 15):
            self.bottle()
            self.bottle_number = (self.bottle_number + 1) % 8
            self.attack_timer = 0

        if self.phase == 1:
            if self.dir == 1:
                self.x += 0.5
                if self.x == 660:
                    self.dir = -1
            else:
                self.x -= 0.5
                if self.x == 300:
                    self.dir = 1

        elif self.phase == 2:
            if self.speed_control > 5:
                self.angle += 1
                self.angle = self.angle % 360
                self.x += self.radius * math.cos(self.angle * pi / 180)
                self.y += self.radius * math.sin(self.angle * pi / 180)
                if 90 <= self.angle <= 270:
                    self.dir = -1
                else:
                    self.dir = 1
                self.speed_control = 0

        else:
            if self.speed_control > 5:
                if self.dir == 1:
                    self.x += random.randint(1, 10)
                    if self.x >= 870:
                        self.dir = -1
                else:
                    self.x -= random.randint(1, 10)
                    if self.x <= 90:
                        self.dir = 1

                if self.y_direction == 1:
                    self.y += random.randint(1,10)
                    if self.y >= 470:
                        self.y_direction = -1
                else:
                    self.y -= random.randint(1, 10)
                    if self.y <= 90:
                        self.y_direction = 1
                self.speed_control = 0

    def draw(self):
        if self.phase == 3:
            if self.dir == 1:
                self.image.clip_draw(self.frame * 64, 384, 64, 64, self.x, self.y, 200, 200)
            else:
                self.image.clip_draw(self.frame * 64, 448, 64, 64, self.x, self.y, 200, 200)

        else:
            if self.dir == 1:
                self.image.clip_draw(self.frame * 64, 512, 64, 64, self.x, self.y, 200, 200)
            else:
                self.image.clip_draw(self.frame * 64, 576, 64, 64, self.x, self.y, 200, 200)

    def bottle(self):
        bottle = Bottle(self.x, self.y, self.phase, self.bottle_number)
        game_world.add_object(bottle, 1)
