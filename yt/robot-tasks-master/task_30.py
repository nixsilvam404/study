#!/usr/bin/python3

from pyrob.api import *


def move(n):
    for i in range(n):
        move_right()
        fill_cell()
    move_right()
    for i in range(n):
        move_down()
        fill_cell()
    move_down()
    for i in range(n):
        move_left()
        fill_cell()
    move_left()
    for i in range(n):
        move_up()
        fill_cell()
    move_up()


def count():
    nn = 1
    while not wall_is_on_the_right():
        move_right()
        nn += 1
    while not wall_is_on_the_left():
        move_left()
    return nn - 2


@task(delay=0.01)
def task_9_3():
    n = count()
    if n > 0:
        for i in range(n):
            move(n)
            move_down()
            move_right()
            n -= 2
    while not wall_is_beneath():
        move_down()
    while not wall_is_on_the_left():
        move_left()


if __name__ == '__main__':
    run_tasks()
