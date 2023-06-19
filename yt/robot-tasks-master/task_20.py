#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    move_right()
    for i in range(6):
        while wall_is_on_the_right() is False:
            fill_cell()
            move_right()
        if wall_is_on_the_right():
            move_down()
            move_left()
        while wall_is_on_the_left() is False:
            fill_cell()
            move_left()
        if wall_is_on_the_left():
            move_down()
            move_right()


if __name__ == '__main__':
    run_tasks()
