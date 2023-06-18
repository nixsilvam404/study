#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    if wall_is_above() and wall_is_on_the_left():
        while True:
            move_right()
            move_down()
            if wall_is_on_the_right() and wall_is_beneath():
                break
    elif wall_is_above() and wall_is_on_the_right():
        while True:
            move_left()
            move_down()
            if wall_is_on_the_left() and wall_is_beneath():
                break
    elif wall_is_on_the_left():
        while True:
            move_right()
            move_up()
            if wall_is_on_the_right() and wall_is_above():
                break
    else:
        while True:
            move_left()
            move_up()
            if wall_is_on_the_left() and wall_is_above():
                break


if __name__ == '__main__':
    run_tasks()
