from pico2d import *
import random
from project.game_code.state_code import main_state
from project.game_code.object_code import game_world
from project.game_code.object_code.bottle import Bottle


class Drunk:
    def __init__(self, x=480, y=300):
        self.x, self.y = x, y
        self.frame = 0
        self.dir = 1
        self.frame_speed_control = 0
        self.phase = 1
        self.is_hit = False
        self.image = load_image('sprite\\Enemy\\boss.png')
        self.hp = 200
        self.bottle_number = 0
        self.attack_timer = 0

    def update(self):
        self.frame_speed_control += 1
        self.attack_timer += 1
        if self.frame_speed_control > 50:
            self.frame = (self.frame + 1) % 8
            self.frame_speed_control = 0

        if self.hp >= 150:
            self.phase = 1
        elif self.hp >= 60:
            self.phase = 2
        else:
            self.phase = 3

        if self.attack_timer > 100 - (self.phase * 15):
            Bottle(self.x, self.y, self.phase, self.bottle_number)
            self.bottle_number = (self.bottle_number + 1) % 8
            self.attack_timer = 0

    def draw(self):
        if self.is_hit:
            self.image.clip_draw(self.frame * 64, 512, 64, 64, self.x, self.y, 200, 200)

        else:
            if self.dir == 1:
                self.image.clip_draw(self.frame * 64, 512, 64, 64, self.x, self.y, 200, 200)
            else:
                self.image.clip_draw(self.frame * 64, 576, 32, 32, self.x, self.y, 200, 200)

#  def bottle(self):
#      bottle = Bottle(self.x, self.y, self.phase, self.bottle_number)
#    game_world.add_object(bottle, 3)
#     self.bottle_number = (self.bottle_number + 1) % 8
