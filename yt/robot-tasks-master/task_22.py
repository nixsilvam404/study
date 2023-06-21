#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    while True:
        while not wall_is_on_the_right() and not wall_is_beneath():
            fill_cell()
            move_right()
        if wall_is_on_the_right() and not wall_is_beneath():
            fill_cell()
            move_down()
        while not wall_is_on_the_left() and not wall_is_beneath():
            fill_cell()
            move_left()
        if wall_is_on_the_left() and not wall_is_beneath():
            fill_cell()
            move_down()
        while not wall_is_on_the_right() and wall_is_beneath() and not cell_is_filled():
            fill_cell()
            move_right()
        while not wall_is_on_the_left() and wall_is_beneath() and not cell_is_filled():
            fill_cell()
            move_left()
        while not wall_is_on_the_left() and wall_is_beneath() and cell_is_filled():
            move_left()
        if wall_is_on_the_left() and wall_is_beneath() and cell_is_filled():
            break
        if wall_is_on_the_right() and wall_is_on_the_left() and wall_is_above() and wall_is_beneath():
            fill_cell()
            break


if __name__ == '__main__':
    run_tasks()
