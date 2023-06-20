#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    while True:
        while wall_is_on_the_right() is False and wall_is_beneath() is False:
            fill_cell()
            move_right()
        if wall_is_on_the_right() and wall_is_beneath() is False:
            fill_cell()
            move_down()
        while wall_is_on_the_left() is False and wall_is_beneath() is False:
            fill_cell()
            move_left()
        if wall_is_on_the_left() and wall_is_beneath() is False:
            fill_cell()
            move_down()
        while wall_is_on_the_right() is False and wall_is_beneath() and cell_is_filled() is False:
            fill_cell()
            move_right()
        while wall_is_on_the_left() is False and wall_is_beneath() and cell_is_filled() is False:
            fill_cell()
            move_left()
        while wall_is_on_the_left() is False and wall_is_beneath() and cell_is_filled():
            move_left()
        if wall_is_on_the_left() and wall_is_beneath() and cell_is_filled():
            break
        if wall_is_on_the_right() and wall_is_on_the_left() and wall_is_above() and wall_is_beneath():
            fill_cell()
            break
        else:
            break


if __name__ == '__main__':
    run_tasks()
