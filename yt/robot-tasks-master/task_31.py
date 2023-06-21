#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    x = 0
    while True:
        while not wall_is_on_the_right():
            move_right()
        while not wall_is_beneath():
            move_down()
        while wall_is_beneath():
            move_left()
            if not wall_is_beneath():
                move_down()
                x = 1
        if x == 0:
            break





if __name__ == '__main__':
    run_tasks()
