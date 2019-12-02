from pico2d import *
import time
from project.game_code.object_code.bubble import Bubble
from project.game_code.management_code import game_world
from project.game_code.state_code import game_framework

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, CTRL, SPACE = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_LCTRL): CTRL,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 30.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4


class IdleState:
    @staticmethod
    def enter(Dragon, event):
        if event == SPACE:
            if not Dragon.is_jump:
                Dragon.is_jump = True
                Dragon.is_fall = False
                Dragon.jump_speed = Dragon.speed * game_framework.frame_time
                Dragon.jump_y = Dragon.y + 120
        if event == RIGHT_DOWN:
            Dragon.velocity += Dragon.speed
        elif event == LEFT_DOWN:
            Dragon.velocity -= Dragon.speed
        elif event == RIGHT_UP:
            Dragon.velocity -= Dragon.speed
        elif event == LEFT_UP:
            Dragon.velocity += Dragon.speed
        if event == CTRL:
            Dragon.is_attack = True

    @staticmethod
    def exit(Dragon, event):
        pass

    @staticmethod
    def do(Dragon):
        Dragon.frame = (Dragon.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 16
        if Dragon.is_jump:
            if not Dragon.is_fall:
                Dragon.y += Dragon.jump_speed
                if Dragon.y >= Dragon.jump_y:
                    Dragon.is_fall = True
            elif Dragon.is_fall:
                Dragon.y -= Dragon.jump_speed

        if Dragon.is_attack:
            Dragon.attack_time += 1
            if Dragon.attack_time > 100:
                Dragon.is_attack = 0
                Dragon.attack_time = 0

        if Dragon.is_beaten:
            Dragon.invincible_check_time = get_time() - Dragon.invincible_start_time
            if Dragon.invincible_check_time > 0.5:
                Dragon.is_beaten = False



    @staticmethod
    def draw(Dragon):
        if Dragon.is_beaten:
            if Dragon.dir > 0:
                Dragon.image.clip_draw(0, 96, 16, 16, Dragon.x, Dragon.y, 50, 50)
            else:
                Dragon.image.clip_draw(0, 112, 16, 16, Dragon.x, Dragon.y, 50, 50)

        else:
            if Dragon.is_attack:
                if Dragon.dir > 0:
                    Dragon.image.clip_draw(int(Dragon.frame) * 16, 64, 16, 16, Dragon.x, Dragon.y, 50, 50)
                else:
                    Dragon.image.clip_draw(int(Dragon.frame) * 16, 80, 16, 16, Dragon.x, Dragon.y, 50, 50)


            else:
                if not Dragon.is_jump:
                    if Dragon.dir > 0:
                        Dragon.image.clip_draw(int(Dragon.frame) * 16, 32, 16, 16, Dragon.x, Dragon.y, 50, 50)
                    else:
                        Dragon.image.clip_draw(int(Dragon.frame) * 16, 48, 16, 16, Dragon.x, Dragon.y, 50, 50)

                elif Dragon.is_jump:
                    if Dragon.dir > 0:
                        Dragon.image.clip_draw(int(Dragon.frame) * 16, 0, 16, 16, Dragon.x, Dragon.y, 50, 50)
                    else:
                        Dragon.image.clip_draw(int(Dragon.frame) * 16, 16, 16, 16, Dragon.x, Dragon.y, 50, 50)


class RunState:
    @staticmethod
    def enter(Dragon, event):
        if event == SPACE:
            if not Dragon.is_jump:
                Dragon.is_jump = True
                Dragon.is_fall = False
                Dragon.jump_speed = Dragon.speed * game_framework.frame_time
                Dragon.jump_y = Dragon.y + 120
        if event == RIGHT_DOWN:
            Dragon.velocity += Dragon.speed
        elif event == LEFT_DOWN:
            Dragon.velocity -= Dragon.speed
        elif event == RIGHT_UP:
            Dragon.velocity -= Dragon.speed
        elif event == LEFT_UP:
            Dragon.velocity += Dragon.speed
        if event == CTRL:
            Dragon.is_attack = True
        Dragon.dir = Dragon.velocity

    @staticmethod
    def exit(Dragon, event):
        pass

    @staticmethod
    def do(Dragon):
        Dragon.frame = (Dragon.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 16

        Dragon.x += Dragon.velocity * game_framework.frame_time
        Dragon.x = clamp(70, Dragon.x, 960 - 70)

        if Dragon.is_jump:
            if not Dragon.is_fall:
                Dragon.y += Dragon.jump_speed
                if Dragon.y >= Dragon.jump_y:
                    Dragon.is_fall = True
            elif Dragon.is_fall:
                Dragon.y -= Dragon.jump_speed

        if Dragon.is_attack:
            Dragon.attack_time += 1
            if Dragon.attack_time > 100:
                Dragon.is_attack = False
                Dragon.attack_time = 0

        if Dragon.is_beaten:
            Dragon.invincible_check_time = get_time() - Dragon.invincible_start_time
            if Dragon.invincible_check_time > 0.5:
                Dragon.is_beaten = False

    @staticmethod
    def draw(Dragon):
        if Dragon.is_beaten:
            if Dragon.dir > 0:
                Dragon.image.clip_draw(0, 96, 16, 16, Dragon.x, Dragon.y, 50, 50)
            else:
                Dragon.image.clip_draw(0, 112, 16, 16, Dragon.x, Dragon.y, 50, 50)
        else:
            if Dragon.is_attack:
                if Dragon.dir > 0:
                    Dragon.image.clip_draw(int(Dragon.frame) * 16, 64, 16, 16, Dragon.x, Dragon.y, 50, 50)
                else:
                    Dragon.image.clip_draw(int(Dragon.frame) * 16, 80, 16, 16, Dragon.x, Dragon.y, 50, 50)

            else:
                if not Dragon.is_jump:
                    if Dragon.velocity > 0:
                        Dragon.image.clip_draw(int(Dragon.frame) * 16, 128, 16, 16, Dragon.x, Dragon.y, 50, 50)
                    else:
                        Dragon.image.clip_draw(int(Dragon.frame) * 16, 144, 16, 16, Dragon.x, Dragon.y, 50, 50)

                else:
                    if Dragon.dir > 0:
                        Dragon.image.clip_draw(int(Dragon.frame) * 16, 0, 16, 16, Dragon.x, Dragon.y, 50, 50)
                    else:
                        Dragon.image.clip_draw(int(Dragon.frame) * 16, 16, 16, 16, Dragon.x, Dragon.y, 50, 50)


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState,
                LEFT_DOWN: RunState, CTRL: IdleState, SPACE: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState,
               RIGHT_DOWN: IdleState, CTRL: RunState, SPACE: RunState}

}


class Dragon:
    def __init__(self):
        self.x, self.y = 100, 100
        self.jump_y = 0
        self.image = load_image('sprite\\Character\\character.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.is_attack = False
        self.attack_time = 0
        self.speed = RUN_SPEED_PPS
        self.is_beaten = False
        self.is_jump = False
        self.is_fall = True
        self.check_attack_delay_start_time = 0
        self.check_attack_delay_end_time = 0
        self.jump_speed = RUN_SPEED_PPS * game_framework.frame_time
        self.is_beaten = False
        self.life = 3
        self.invincible_start_time = 0
        self.invincible_check_time = 0
        self.gold = 0

    def update_state(self, state):
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
      #  draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def stop(self):
        self.jump_speed = 0
        self.is_jump = False

    def cancel_stop(self):
        self.jump_speed = RUN_SPEED_PPS * game_framework.frame_time
        self.is_jump = True




