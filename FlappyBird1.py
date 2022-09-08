from jguvc_eip import basic_io as bio
from jguvc_eip import image_objects as io
from jguvc_eip.colors import *
from time import sleep
import random

# constant stuff
fig_field_x = 100
fig_field_y = 0

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
random1 = random.randint(0, 250)
random2 = random.randint(0, 250)
random3 = random.randint(0, 250)
random4 = random.randint(0, 250)

# extras
speed_obstacles = 0

y = 0

if __name__ == "__main__":

    bio.start()

    bio.resize_image(700, 350)


    # bob = bio.load_image("bob.png")

    def obstical(pos_obstacles_1, randomint1):
        obstacle_1a = io.Rectangle(20, randomint1, fill_color=BLACK)
        obstacle_1b = io.Rectangle(20, 100, fill_color=None, border_color=None)
        obstacle_1c = io.Rectangle(20, abs(randomint1 - 300), fill_color=BLACK)
        obstacle_1 = io.VerticalStack([obstacle_1a, obstacle_1b, obstacle_1c])
        obstacle_1 = io.Translate(obstacle_1, 0, 0)
        bio.draw_object(obstacle_1, pos_obstacles_1, 0)


    def check(pos_obstc, pos_fig, rnd):
        if pos_obstc >= 80 and pos_obstc <= 115:
            # bio.draw_text(200, 200, "TEST")
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


    while True:
        # double buffering
        bio.set_active_image(db_active_buffer)
        bio.set_visible_image(db_visible_buffer)
        bio.copy_image(db_visible_buffer, db_active_buffer)
        db_visible_buffer, db_active_buffer = db_active_buffer, db_visible_buffer

        bio.clear_image()

        # bio.draw_image(0, 0, bob)

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
        obstical(pos_obstacles_1, random1)
        obstical(pos_obstacles_2, random2)
        obstical(pos_obstacles_3, random3)
        obstical(pos_obstacles_4, random4)

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
            random1 = random.randint(0, 250)
            pos_obstacles_1 = 800
        if pos_obstacles_2 <= 0:
            random2 = random.randint(0, 250)
            pos_obstacles_2 = 800
        if pos_obstacles_3 <= 0:
            random3 = random.randint(0, 250)
            pos_obstacles_3 = 800
        if pos_obstacles_4 <= 0:
            random4 = random.randint(0, 250)
            pos_obstacles_4 = 800

        # check if figure hit obstacle
        check(pos_obstacles_1, pos_figure, random1)
        check(pos_obstacles_2, pos_figure, random2)
        check(pos_obstacles_3, pos_figure, random3)
        check(pos_obstacles_4, pos_figure, random4)

        # creating figure
        figure = io.Rectangle(20, 20, fill_color=BLUE)
        figure = io.Translate(figure, 0, int(pos_figure))

        # draw figure
        bio.draw_object(figure, fig_field_x, fig_field_y)

        sleep(0.016)
