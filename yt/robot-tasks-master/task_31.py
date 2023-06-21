#!/usr/bin/python3

from pyrob.api import *


def count():
    n = 1
    while not wall_is_on_the_left():
        move_left()
    while not wall_is_on_the_right():
        move_right()
        n += 1
    return n


@task(delay=0.01)
def task_8_30():
    n = count()
    x = 1
    while x != n:
        while not wall_is_on_the_right():
            move_right()
        while not wall_is_beneath():
            move_down()
        while wall_is_beneath() and x != n:
            move_left()
            x += 1
        while not wall_is_beneath():
            move_down()
            x = 1


if __name__ == '__main__':
    run_tasks()
