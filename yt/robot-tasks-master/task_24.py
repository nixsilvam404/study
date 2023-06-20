#!/usr/bin/python3

from pyrob.api import *


def christ():
    fill_cell()
    move_down()
    fill_cell()
    move_down()
    fill_cell()
    move_right()
    move_up()
    fill_cell()
    move_left(2)
    fill_cell()
    move_up()


@task
def task_2_1():
    move_down()
    move_right(2)
    christ()


if __name__ == '__main__':
    run_tasks()
