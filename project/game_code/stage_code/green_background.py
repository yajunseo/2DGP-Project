from pico2d import *


class Background:
    def __init__(self):
        self.image = load_image('sprite\\map\\stage3 - 복사본.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(480, 300, 960, 600)
        for brick in self.get_bb():
            draw_rectangle(*brick)

    def get_bb(self):
        return [[1, 1, 200, 25],
                [360, 1, 600, 25],
                [760, 1, 960 - 1, 25],
                [120, 105, 225, 130],
                [430, 105, 535, 130],
                [743, 105, 848, 130],
                [215, 215, 320, 240],
                [433, 215, 538, 240],
                [651, 215, 756, 240],
                [120, 324, 225, 349],
                [430, 324, 535, 349],
                [743, 324, 848, 349],
                [215, 430, 320, 455],
                [648, 430, 754, 455],
                ]


