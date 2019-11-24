from pico2d import *


class Background:
    def __init__(self):
        self.image = load_image('sprite\\map\\boss_stage.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(480, 300, 960, 600)
    #    for brick in self.get_bb():
    #        draw_rectangle(*brick)

    def get_bb(self):
        return [[0, 0, 960 - 1, 25],
                [45, 107, 172, 132],
                [793, 107, 915, 132],
                [45, 215, 173, 240],
                [793, 215, 915, 240],
                [40, 323, 174, 348],
                [793, 323, 915, 348],
                [45, 431, 145, 456],
                [818, 431, 915, 456],
                [265, 107, 700, 132],
                [265, 215, 700, 240],
                [265, 323, 700, 348]
                ]