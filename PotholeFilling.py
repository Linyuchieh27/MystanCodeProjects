"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre_condition:Karel is at the(2,1)
    Post_condition:Karel is at the(2,7)
    """
    for i in range(3):
        go_in()
        put_99()
        go_out()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def put_99():
    """
    Karel will put 99 beepers
    """
    for i in range(99):
        put_beeper()


def turn_around():
    turn_left()
    turn_left()


def go_in():
    """
    Pre_condition:Karel is at the upper left of the pothole facing East
    Post_condition:Karel is in the pothole facing South
    """
    move()
    turn_right()
    move()


def go_out():
    """
    Pre_condition:Karel is in the pothole facing South
    Post_condition:Karel is at the upper left of the pothole facing East
    """
    turn_around()
    move()
    turn_right()
    move()

# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
