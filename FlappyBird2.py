from jguvc_eip import basic_io as bio
from jguvc_eip import image_objects as io
from jguvc_eip.colors import *
from time import sleep
import random

# constant stuff
fig_field_x = 100
fig_field_y = 0
background_x = -130
var = 0
a = 0
b = 0
c = 0
d = 0
aa = 0
bb = 0
cc = 0
dd = 0


# beginning game score
points = 0
coin_points = 0

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

# pos of coins
pos_coin_1 = 900
pos_coin_2 = 1300
pos_coin_3 = 1700
pos_coin_4 = 2100

# random numbers generator coins
coin_random1 = random.randint(0, 250)
coin_random2 = random.randint(0, 250)
coin_random3 = random.randint(0, 250)
coin_random4 = random.randint(0, 250)

# random numbers generator
random1 = random.randint(0, 250)
random2 = random.randint(0, 250)
random3 = random.randint(0, 250)
random4 = random.randint(0, 250)

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
    fish_dead = bio.load_image('fish_dead.png')


    def coins(pos_coin_1, randomint1):
        coin = io.Circle(20, fill_color=ORANGE)
        bio.draw_object(coin, pos_coin_1, randomint1)

    def check(pos_obstc, pos_fig, rnd):
        if pos_obstc >= 80 and pos_obstc <= 115:
            bio.draw_text(610, 0, "Score: ", color = GREEN)
            bio.draw_text(675, 0, str(points), color = GREEN)
            if pos_fig <= rnd - 1:
                if points < 11:
                    bio.print_message("GAME OVER!!! Score: " + str(points) + "  Coins: " + str(coin_points)) + bio.print_message("Skill Level: Noob")
                if points > 10 and points < 26:
                    bio.print_message("GAME OVER!!! Score: " + str(points) + "  Coins: " + str(coin_points)) + bio.print_message("Skill Level: Amateur")
                if points > 25 and points < 51:
                    bio.print_message("GAME OVER!!! Score: " + str(points) + "  Coins: " + str(coin_points)) + bio.print_message("Skill Level: Good")
                if points > 50 and points < 100:
                    bio.print_message("GAME OVER!!! Score: " + str(points) + "  Coins: " + str(coin_points)) + bio.print_message("Skill Level: Professional")
                if points > 99:
                    bio.print_message("GAME OVER!!! Score: " + str(points) + "  Coins: " + str(coin_points)) + bio.print_message("Skill Level: Advanced Being")

            elif pos_fig >= rnd + 80:
                if points < 11:
                    bio.print_message("GAME OVER!!! Score: " + str(points) + "  Coins: " + str(coin_points)) + bio.print_message("Skill Level: Noob")
                if points > 10 and points < 26:
                    bio.print_message("GAME OVER!!! Score: " + str(points) + "  Coins: " + str(coin_points)) + bio.print_message("Skill Level: Amateur")
                if points > 25 and points < 51:
                    bio.print_message("GAME OVER!!! Score: " + str(points) + "  Coins: " + str(coin_points)) + bio.print_message("Skill Level: Good")
                if points > 50 and points < 100:
                    bio.print_message("GAME OVER!!! Score: " + str(points) + "  Coins: " + str(coin_points)) + bio.print_message("Skill Level: Professional")
                if points > 99:
                    bio.print_message("GAME OVER!!! Score: " + str(points) + "  Coins: " + str(coin_points)) + bio.print_message("Skill Level: Advanced Being")


    def check_coin(pos_coin, pos_fig, rnd):
        if pos_coin >= 80 and pos_coin <= 115:
            if pos_fig <= rnd + 10 and pos_fig >= rnd - 20:
                bio.draw_text(610, 15, "Coins: ", color=GREEN)
                bio.draw_text(675, 15, str(coin_points), color=GREEN)
                return True


    def score(pos_obstc, points):
        bio.draw_text(610, 0, "Score: ", color=YELLOW)
        bio.draw_text(675, 0, str(points), color=YELLOW)
        if pos_obstc == 80 or pos_obstc == 79 or pos_obstc == 78:
            points = points + 1
        return points

    def score_coins(pos_coin, coin_points):
        bio.draw_text(610, 15, "Coins: ", color=YELLOW)
        bio.draw_text(675, 15, str(coin_points), color=YELLOW)
        if pos_coin == pos_figure + 3 or pos_coin == pos_figure + 2 or pos_coin == pos_figure + 1:
            coin_points += 1
        return coin_points

    while True:
        # double buffering
        bio.set_active_image(db_active_buffer)
        bio.set_visible_image(db_visible_buffer)
        bio.copy_image(db_visible_buffer, db_active_buffer)
        db_visible_buffer, db_active_buffer = db_active_buffer, db_visible_buffer

        bio.clear_image()

        # background
        bio.draw_image(background_x, -100, background)

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
        bio.draw_image(pos_obstacles_1 -2, random1 + 100, pipe_bottom)
        bio.draw_image(pos_obstacles_1 - 2, random1 - 349, pipe_top)
        bio.draw_image(pos_obstacles_2 - 2, random2 + 100, pipe_bottom)
        bio.draw_image(pos_obstacles_2 -2, random2 - 349, pipe_top)
        bio.draw_image(pos_obstacles_3 - 2, random3 + 100, pipe_bottom)
        bio.draw_image(pos_obstacles_3 -2, random3 - 349, pipe_top)
        bio.draw_image(pos_obstacles_4 - 2, random4 + 100, pipe_bottom)
        bio.draw_image(pos_obstacles_4 -2, random4 - 349, pipe_top)

        # creating coins
        if a == 0:
            coins(pos_coin_1, coin_random1)
        if check_coin(pos_coin_1, pos_figure, coin_random1) and a == 0:
            aa = 1
            coin_points += 1
        if aa == 1:
            a += 1
        if a == 100:
            aa = 0
            a = 0

        if b == 0:
            coins(pos_coin_2, coin_random2)
        if check_coin(pos_coin_2, pos_figure, coin_random2) and b == 0:
            bb = 1
            coin_points += 1
        if bb == 1:
            b += 1
        if b == 100:
            bb = 0
            b = 0

        if c == 0:
            coins(pos_coin_3, coin_random3)
        if check_coin(pos_coin_3, pos_figure, coin_random3) and c == 0:
            cc = 1
            coin_points += 1
        if cc == 1:
            c += 1
        if c == 100:
            cc = 0
            c = 0

        if d == 0:
            coins(pos_coin_4, coin_random4)
        if check_coin(pos_coin_4, pos_figure, coin_random4) and d == 0:
            dd = 1
            coin_points += 1
        if dd == 1:
            d += 1
        if d == 100:
            dd = 0
            d = 0

        # score counting
        points = score(pos_obstacles_1, points)
        points = score(pos_obstacles_2, points)
        points = score(pos_obstacles_3, points)
        points = score(pos_obstacles_4, points)

        coin_points = score_coins(pos_coin_1, coin_points)
        coin_points = score_coins(pos_coin_2, coin_points)
        coin_points = score_coins(pos_coin_3, coin_points)
        coin_points = score_coins(pos_coin_4, coin_points)

        # obstacles moving to the left
        pos_obstacles_1 -= 3
        pos_obstacles_2 -= 3
        pos_obstacles_3 -= 3
        pos_obstacles_4 -= 3

        # coins moving to the left
        pos_coin_1 -= 3
        pos_coin_2 -= 3
        pos_coin_3 -= 3
        pos_coin_4 -= 3

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

        # random coin infinite spawn
        if pos_coin_1 <= 0:
            coin_random1 = random.randint(0, 250)
            pos_coin_1 = 1600
        if pos_coin_2 <= 0:
            coin_random2 = random.randint(0, 250)
            pos_coin_2 = 1600
        if pos_coin_3 <= 0:
            coin_random3 = random.randint(0, 250)
            pos_coin_3 = 1600
        if pos_coin_4 <= 0:
            coin_random4 = random.randint(0, 250)
            pos_coin_4 = 1600

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