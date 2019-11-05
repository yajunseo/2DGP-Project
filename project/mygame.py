import pico2d
from project.game_code.state_code import game_framework
from project.game_code.state_code import start_state

pico2d.open_canvas(960, 600)
game_framework.run(start_state)
pico2d.close_canvas()