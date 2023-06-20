#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    move_right()
    while wall_is_on_the_right() is False and wall_is_beneath():
        if wall_is_above() is False and wall_is_beneath():
            move_up()
            fill_cell()
            while wall_is_on_the_right() and wall_is_on_the_left() and wall_is_above() is False:
                move_up()
                fill_cell()
        if wall_is_on_the_right() and wall_is_on_the_left() and wall_is_above():
            move_down()
        while cell_is_filled():
            move_down()
        move_right()
    # last tunel begin
    if wall_is_on_the_right() and wall_is_above() is False and wall_is_beneath():
        move_up()
        fill_cell()
    while wall_is_on_the_right() and wall_is_on_the_left() and wall_is_above() is False:
        move_up()
        fill_cell()
    if wall_is_on_the_right() and wall_is_on_the_left() and wall_is_above():
        move_down()
    while cell_is_filled():
        move_down()
    # last tunel end
    if wall_is_on_the_right() and wall_is_beneath():
        move_left()
    while wall_is_beneath():
        move_left()


if __name__ == '__main__':
    run_tasks()
