#!/usr/bin/python3

from pyrob.api import *


def right_down():
    move_right()
    move_down()


@task
def task_1_2():
    for i in range(2):
        right_down()
    fill_cell()
    right_down()
    move_right()


if __name__ == '__main__':
    run_tasks()
