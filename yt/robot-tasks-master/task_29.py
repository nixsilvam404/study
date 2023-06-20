#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    n = 0
    while not wall_is_on_the_right():
        if cell_is_filled():
            n += 1
        if n == 3:
            break
        move_right()
        if not cell_is_filled():
            n = 0


if __name__ == '__main__':
    run_tasks()
