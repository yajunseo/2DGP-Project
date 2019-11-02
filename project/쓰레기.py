class JumpState:
    t = 0
    p1, p2, p3 = (0, 0), (0, 0), (0, 0)
    temp_x, temp_y = 0, 0

    @staticmethod
    def enter(Dragon, event):
        if event == SPACE_DOWN:
            Dragon.jump_y = Dragon.y + 200
            if Dragon.velocity > 0:
                Dragon.jump_x = Dragon.x + 200
            elif Dragon.velocity < 0:
                Dragon.jump_x = Dragon.x - 200
            else:
                Dragon.jump_x = Dragon.x
            JumpState.p1, JumpState.p2, JumpState.p3 = (Dragon.x, Dragon.y), ((Dragon.jump_x + Dragon.x) / 2, Dragon.jump_y), (Dragon.jump_x, Dragon.y)

    @staticmethod
    def exit(Dragon, event):
        pass

    @staticmethod
    def do(Dragon):
      while JumpState.t <= (998 / 1000):
            Dragon.frame_speed += 1
            if Dragon.frame_speed > 30:
                Dragon.frame = (Dragon.frame + 1) % 16
                Dragon.frame_speed = 0

            for i in range(0, 1000 + 1, 2):
                JumpState.t = i / 1000
                JumpState.temp_x = (2 * JumpState.t ** 2 - 3 * JumpState.t + 1) * JumpState.p1[0] + (-4 * JumpState.t ** 2 + 4 * JumpState.t) * JumpState.p2[0] + (2 * JumpState.t ** 2 - JumpState.t) * JumpState.p3[0]
                JumpState.temp_y = (2 * JumpState.t ** 2 - 3 * JumpState.t + 1) * JumpState.p1[1] + (-4 * JumpState.t ** 2 + 4 * JumpState.t) * JumpState.p2[1] + (2 * JumpState.t ** 2 - JumpState.t) * JumpState.p3[1]
                JumpState.temp_x = clamp(70, Dragon.x, 960 - 70)
                Dragon.x = JumpState.temp_x
                Dragon.y = JumpState.temp_y
                if Dragon.dir == 1:
                    Dragon.image.clip_draw(Dragon.frame * 16, 0, 16, 16, Dragon.x, Dragon.y, 60, 60)
                else:
                    Dragon.image.clip_draw(Dragon.frame * 16, 16, 16, 16, Dragon.x, Dragon.y, 60, 60)


    @staticmethod
    def draw(Dragon):
        if Dragon.dir == 1:
            Dragon.image.clip_draw(Dragon.frame * 16, 0, 16, 16, Dragon.x, Dragon.y, 60, 60)
        else:
            Dragon.image.clip_draw(Dragon.frame * 16, 16, 16, 16, Dragon.x, Dragon.y, 60, 60)
