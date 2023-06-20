#!/usr/bin/python3

from pyrob.api import *
from task_24 import christ


def christs(x):
    for i in range(x):
        christ()
        move_right(5)
    christ()


@task
def task_2_2():
    x = 4
    move_right()
    move_down()
    christs(x)


if __name__ == '__main__':
    run_tasks()
