#!/usr/bin/python3

from pyrob.api import *
from task_25 import christs


def left():
    while wall_is_on_the_left() is False:
        move_left()


@task(delay=0.02)
def task_2_4():
    x = 9
    for i in range(4):
        move_right()
        christs(x)
        move_down(4)
        left()
    move_right()
    christs(x)
    left()


if __name__ == '__main__':
    run_tasks()
