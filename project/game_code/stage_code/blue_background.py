from pico2d import *


class Background:
    def __init__(self):
        self.image = load_image('sprite\\map\\map1-1.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(480, 300, 960, 600)
        for brick in self.get_bb():
            draw_rectangle(*brick)

    def get_bb(self):
        return [[0, 0, 960 - 1, 25],
                [198, 110, 438, 130],
                [533, 110, 768, 130],
                [150, 195, 368, 215],
                [603, 195, 823, 215],
                [198, 280, 438, 300],
                [533, 280, 773, 300],
                [265, 365, 705, 385]]


