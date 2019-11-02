from pico2d import *
import random


class Monster1:
    image = None
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.turn = random.randint(-100, 100)
        self.frame = random.randint(0, 12)
        self.dir = 1
        self.frame_speed = 0
        if self.image == None:
            self.image = load_image('sprite\\Enemy\\walker.png')


    def update(self):
        self.frame_speed += 1
        if self.frame_speed > 30:
            self.frame = (self.frame + 1) % 12
            self.frame_speed = 0
        self.turn += 1
        if self.turn >= 0:
            self.dir = 1
            self.x += 1
            self.x = clamp(70, self.x, 960 - 70)
            if self.turn >= 100:
                self.turn = - 100
        if self.turn < 0:
            self.dir = -1
            self.x -= 1
            self.x = clamp(70, self.x, 960 - 70)

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame * 16, 224, 16, 16, self.x, self.y, 50, 50)
        else:
            self.image.clip_draw(self.frame * 16, 240, 16, 16, self.x, self.y, 50, 50)



