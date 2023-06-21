#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    while not wall_is_on_the_right() and wall_is_above() and wall_is_beneath():
        move_right()
    while not wall_is_on_the_left() and wall_is_above() and wall_is_beneath():
        move_left()
    while wall_is_above() is False:
        move_up()
    while wall_is_on_the_left() is False:
        move_left()


if __name__ == '__main__':
    run_tasks()
