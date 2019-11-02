from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('sprite\\map1-1.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(480, 300, 960, 600)
