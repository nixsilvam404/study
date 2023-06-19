#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    n = 13
    move_down()
    move_right()
    while n > 1:
        for i in range(n):
            fill_cell()
            move_right()
            move_down()
        n -= 1
        move_left(2)
        move_up()
        for i in range(n):
            fill_cell()
            move_left()
            move_up()
        n -= 1
        move_down(2)
        move_right()
    fill_cell()
    move_down()


if __name__ == '__main__':
    run_tasks()
