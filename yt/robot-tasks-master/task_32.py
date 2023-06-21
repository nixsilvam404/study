#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    x = 0
    while not wall_is_on_the_right():
        if cell_is_filled():
            x += 1
        if wall_is_above() and wall_is_beneath():
            fill_cell()
        move_right()
        if not wall_is_above() and wall_is_beneath():
            move_up()
            while wall_is_on_the_right() and wall_is_on_the_left() and not wall_is_above():
                if cell_is_filled():
                    x += 1
                else:
                    fill_cell()
                move_up()
        if wall_is_on_the_right() and wall_is_on_the_left() and wall_is_above():
            if cell_is_filled():
                x += 1
            else:
                fill_cell()
            move_down()
        while cell_is_filled():
            move_down()
    mov('ax', x)


if __name__ == '__main__':
    run_tasks()
