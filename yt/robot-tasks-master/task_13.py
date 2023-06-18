#!/usr/bin/python3

from pyrob.api import *


def up():
    move_up()
    fill_cell()
    move_down()


def down():
    move_down()
    fill_cell()
    move_up()


def updown():
    move_down()
    fill_cell()
    move_up(2)
    fill_cell()
    move_down()


@task
def task_8_10():
    while True:
        if wall_is_on_the_right() is False and wall_is_above() is False and wall_is_beneath():
            up()
            move_right()
        elif wall_is_on_the_right() is False and wall_is_above() and wall_is_beneath() is False:
            down()
            move_right()
        elif wall_is_on_the_right() is False and wall_is_above():
            move_right()
        elif wall_is_on_the_right() is False:
            updown()
            move_right()
        elif wall_is_on_the_right() and wall_is_above() is False and wall_is_beneath():
            up()
            break
        elif wall_is_on_the_right() and wall_is_above() and wall_is_beneath() is False:
            down()
            break
        elif wall_is_on_the_right() and wall_is_above():
            break
        else:
            updown()
            break


if __name__ == '__main__':
    run_tasks()
