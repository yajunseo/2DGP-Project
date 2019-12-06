from pico2d import *
from project.game_code.state_code import game_framework
from project.game_code.state_code import first_main_state
from project.game_code.state_code import second_main_state
from project.game_code.state_code import third_main_state
from project.game_code.state_code import title_state
import json

name = "EndState"
curtain = None
background = None
font = None
game_clear_font = None
font_score = None
score = None
count = 0
font_restart = None
ranking_list = []
end_sound = None


def enter():
    global curtain, background, font, font_score, game_clear_font, score, count, ranking_list, font_restart, end_sound
    curtain = load_image('sprite\\map\\curtain.png')
    background = load_image('sprite\\map\\check.png')
    game_clear_font = load_font('font.TTF', 70)
    font = load_font('font.TTF', 30)
    font_restart = load_font('font.TTF', 20)
    font_score = load_font('font.TTF', 30)
    count = 0
    score = third_main_state.get_gold()
    with open('ranking_data.json', 'r') as f:
        ranking_list = json.load(f)

    ranking_list.append(score)
    ranking_list.sort(reverse=True)

    with open('ranking_data.json', 'w') as f:
        json.dump(ranking_list, f)

    end_sound = load_wav('sound\\end.wav')
    end_sound.set_volume(50)
    end_sound.repeat_play()


def exit():
    global end_sound
    del end_sound
  #  global image
#    del (image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_r):
                game_framework.change_state(title_state)


def draw():
    global count, score

    clear_canvas()
    find_your_rank = False
    count += 1
    background.draw(480, 300, 960, 600)
    curtain.draw(480, 300, 960, 600)
    if count <= 60:
        game_clear_font.draw(130, 400, 'GAME CLEAR', (255, 0, 0))
    else:
        game_clear_font.draw(130, 400, 'GAME CLEAR', (255, 94, 0))
        if count >= 120:
            count = 0
    font_score.draw(330, 350, 'SCORE: %d' % score, (255, 255, 255))

    for i in range(8):
        if score == ranking_list[i]:
            if not find_your_rank:
                font.draw(330, 280 - i * 30, "#" + str(i + 1) + ".",(255, 0, 0))
                font.draw(430, 280 - i * 30, "%0d" % (ranking_list[i]),(255, 0, 0))
                find_your_rank = True

            else:
                font.draw(330, 280 - i * 30, "#" + str(i + 1) + ".")
                font.draw(430, 280 - i * 30, "%0d" % (ranking_list[i]))
        else:
            font.draw(330, 280 - i * 30, "#" + str(i + 1) + ".")
            font.draw(430, 280 - i * 30, "%0d" % (ranking_list[i]))

        font_restart.draw(300, 500, "press R to restart", (255, 255, 0))
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass
