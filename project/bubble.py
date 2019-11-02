from pico2d import *
import game_world

class Bubble:
    image = None

    def __init__(self, x= 300, y=300, velocity = 1):
        if Bubble.image == None:
            Bubble.image = load_image('sprite\\Effect\\bubbles.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.frame = 0
        self.frame_speed = 0
        self.timer = 0
        self.reflect = 0


    def draw(self):
        if 80 < self.x and self.x < 880:
            self.image.clip_draw(self.frame * 16, 224, 13, 13, self.x, self.y, 40, 40)
        else:
            self.image.clip_draw(0, 192, 14, 16, self.x, self.y, 50, 50)



    def update(self):
        self.timer += 1
        self.frame_speed += 1
        if self.frame_speed > 30:
            self.frame = (self.frame + 1) % 2
            self.frame_speed = 0
        if 80 < self.x and self.x < 890:
            self.x += self.velocity * 2
        if self.x <= 80 or self.x >= 890:
            if self.y < 510:
                if self.reflect == 0:
                    self.y += 0.5
                elif self.reflect == 1:
                    self.y -= 0.5
                if self.y == 509:
                    self.reflect = 1

                if self.reflect == 1 and self.y == 500:
                    self.reflect = 0


        if self.timer == 3000:
            game_world.remove_object(self)

