#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_1():
    while True:
        if wall_is_on_the_right() is False:
            move_right()
        else:
            break


if __name__ == '__main__':
    run_tasks()
