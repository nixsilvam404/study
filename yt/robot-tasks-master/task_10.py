#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_3():
    while True:
        if wall_is_above() is False and wall_is_beneath() is False and wall_is_on_the_right() is False:
            move_right()
        elif wall_is_above() is False and wall_is_beneath() is False and wall_is_on_the_right():
            break
        elif wall_is_above() and wall_is_beneath() and wall_is_on_the_right() or (
            wall_is_above() and wall_is_beneath() is False and wall_is_on_the_right()
        ) or wall_is_above() is False and wall_is_beneath() and wall_is_on_the_right():
            fill_cell()
            break
        else:
            fill_cell()
            move_right()


if __name__ == '__main__':
    run_tasks()
