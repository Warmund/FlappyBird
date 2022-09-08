from jguvc_eip import basic_io as bio
from jguvc_eip import image_objects as io
from jguvc_eip.colors import *
from time import sleep
import random

# constant stuff
fig_field_x = 100
fig_field_y = 0
background_x = 0
var = 0

# beginning game score
points = 0

# double buffering
db_visible_buffer: int = 0
db_active_buffer: int = 1

# figure setting
pos_figure = 100
speed_figure = 0

# settings to play with
accelleration = 0.5
up_bounce = 12

# pos of obstacles
pos_obstacles_1 = 800
pos_obstacles_2 = 1000
pos_obstacles_3 = 1200
pos_obstacles_4 = 1400

# random numbers generator
random1 = random.randint(0, 300)
random2 = random.randint(0, 300)
random3 = random.randint(0, 300)
random4 = random.randint(0, 300)

# extras
speed_obstacles = 0

if __name__ == "__main__":

    bio.start()
    bio.resize_image(700, 350)

    background = bio.load_image('backround_water')
    pipe_bottom = bio.load_image('pipe_bottom.png')
    pipe_top = bio.load_image('pipe_top.png')
    bird_1 = bio.load_image('fish.png')
    bird_2 = bio.load_image('fish.png')

    def check(pos_obstc, pos_fig, rnd):
        if pos_obstc >= 80 and pos_obstc <= 115:
            if pos_fig <= rnd - 1:
                if points < 11:
                    bio.print_message("GAME OVER!!! Score: " + str(points)) + bio.print_message("Skill Level: Noob")
                if points > 10 and points < 26:
                    bio.print_message("GAME OVER!!! Score: " + str(points)) + bio.print_message("Skill Level: Amateur")
                if points > 25 and points < 51:
                    bio.print_message("GAME OVER!!! Score: " + str(points)) + bio.print_message("Skill Level: Good")
                if points > 50 and points < 100:
                    bio.print_message("GAME OVER!!! Score: " + str(points)) + bio.print_message(
                        "Skill Level: Professional")
                if points > 99:
                    bio.print_message("GAME OVER!!! Score: " + str(points)) + bio.print_message(
                        "Skill Level: Advanced Being")

            elif pos_fig >= rnd + 80:
                if points < 11:
                    bio.print_message("GAME OVER!!! Score: " + str(points)) + bio.print_message("Skill Level: Noob")
                if points > 10 and points < 26:
                    bio.print_message("GAME OVER!!! Score: " + str(points)) + bio.print_message("Skill Level: Amateur")
                if points > 25 and points < 51:
                    bio.print_message("GAME OVER!!! Score: " + str(points)) + bio.print_message("Skill Level: Good")
                if points > 50 and points < 100:
                    bio.print_message("GAME OVER!!! Score: " + str(points)) + bio.print_message(
                        "Skill Level: Professional")
                if points > 99:
                    bio.print_message("GAME OVER!!! Score: " + str(points)) + bio.print_message(
                        "Skill Level: Advanced Being")

    def score(pos_obstc, points):
        bio.draw_text(610, 10, "Score: ")
        bio.draw_text(675, 10, str(points))
        if pos_obstc == 80 or pos_obstc == 79 or pos_obstc == 78:
            points = points + 1
        return points

    class pipe(object):
        def __init__(self, x, y, image):
            self.x = x
            self.y = y
            self.image = image
            bio.draw_image(self.x, self.y, self.image)

    while True:
        # double buffering
        bio.set_active_image(db_active_buffer)
        bio.set_visible_image(db_visible_buffer)
        bio.copy_image(db_visible_buffer, db_active_buffer)
        db_visible_buffer, db_active_buffer = db_active_buffer, db_visible_buffer

        bio.clear_image()

        # background / pipe-picture / bird-picture
        bio.draw_image(-130, -100, background)
       # background_x -= 0.5
       # background_x = abs(background_x) % 750
       # background_x = -background_x

        # on button press bump speed_red into negative
        if bio.get_last_key_pressed_event() == " ":
            speed_figure -= up_bounce

        # speed of figure
        speed_figure += accelleration
        pos_figure += speed_figure

        # Luftwiderstand
        speed_figure *= 0.96

        # max speed
        if speed_figure <= -9:
            speed_figure = -9

        # boundary checks
        if pos_figure >= 330:
            pos_figure = 330
            speed_figure = 0

        if pos_figure <= 0:
            pos_figure = 0
            speed_figure = 0

        # creating obstacle
        pipe(pos_obstacles_1 -2, random1 + 100, pipe_bottom)
        pipe(pos_obstacles_1 -2, random1 - 349, pipe_top)
        pipe(pos_obstacles_2 -2, random2 + 100, pipe_bottom)
        pipe(pos_obstacles_2 -2, random2 - 349, pipe_top)
        pipe(pos_obstacles_3 -2, random3 + 100, pipe_bottom)
        pipe(pos_obstacles_3 -2, random3 - 349, pipe_top)
        pipe(pos_obstacles_4 -2, random4 + 100, pipe_bottom)
        pipe(pos_obstacles_4 -2, random4 - 349, pipe_top)

        # score counting
        points = score(pos_obstacles_1, points)
        points = score(pos_obstacles_2, points)
        points = score(pos_obstacles_3, points)
        points = score(pos_obstacles_4, points)

        # obstacles moving to the left
        pos_obstacles_1 -= 3
        pos_obstacles_2 -= 3
        pos_obstacles_3 -= 3
        pos_obstacles_4 -= 3

        # random obstacle infinite spawn
        if pos_obstacles_1 <= 0:
            random1 = random.randint(0, 300)
            pos_obstacles_1 = 800
        if pos_obstacles_2 <= 0:
            random2 = random.randint(0, 300)
            pos_obstacles_2 = 800
        if pos_obstacles_3 <= 0:
            random3 = random.randint(0, 300)
            pos_obstacles_3 = 800
        if pos_obstacles_4 <= 0:
            random4 = random.randint(0, 300)
            pos_obstacles_4 = 800

        # check if figure hit obstacle
        check(pos_obstacles_1, pos_figure, random1)
        check(pos_obstacles_2, pos_figure, random2)
        check(pos_obstacles_3, pos_figure, random3)
        check(pos_obstacles_4, pos_figure, random4)

        # draw figure
        if var == 0:
            bio.draw_image(fig_field_x - 5, pos_figure, bird_1)
            var = 1
        elif var == 1:
            bio.draw_image(fig_field_x - 5, pos_figure, bird_2)
            var = 0

        sleep(0.016)