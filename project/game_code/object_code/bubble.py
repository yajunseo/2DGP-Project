from pico2d import *
import time
from project.game_code.object_code import game_world
from project.game_code.state_code import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 60.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4


class Bubble:
    image = None

    def __init__(self, x=300, y=300, direction=1):
        if Bubble.image is None:
            Bubble.image = load_image('sprite\\Effect\\bubbles.png')
        self.x, self.y, self.dir = x, y, direction
        if direction > 0:
            self.velocity = RUN_SPEED_PPS
        else:
            self.velocity = -RUN_SPEED_PPS
        self.frame = 0
        self.timer = 0
        self.is_reflect = False
        self.check_current_time = 0
        self.check_bubble_create_time = time.time()

    def draw(self):
        if 80 < self.x < 880:
            self.image.clip_draw(int(self.frame) * 16, 224, 13, 13, self.x, self.y, 40, 40)
        else:
            self.image.clip_draw(0, 192, 14, 16, self.x, self.y, 50, 50)

    def update(self):
        self.check_current_time = time.time() - self.check_bubble_create_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

        if 80 < self.x < 890:
            self.x += self.velocity * game_framework.frame_time

        else:
            if self.y < 510:
                if not self.is_reflect:
                    self.y += ((self.velocity**2)**0.5 * game_framework.frame_time)/2
                elif self.is_reflect:
                    self.y -= ((self.velocity**2)**0.5 * game_framework.frame_time)/2
                if self.y >= 509:
                    self.is_reflect = True
                if self.is_reflect and self.y <= 500:
                    self.is_reflect = False

        if self.check_current_time >= 8:
            game_world.remove_object(self)
