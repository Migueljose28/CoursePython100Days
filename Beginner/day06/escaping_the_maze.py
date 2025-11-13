
"""
    I Resolved much challenge the game Reeborg's World.
    The Last tasks to day is it:
    https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
"""


def move():
    """Function belonging to the game"""
    pass


def turn_left():
    pass


def at_goal():
    pass


def front_is_clear():
    pass


def right_is_clear():
    pass


# My code
def turn_right():
    [turn_left() for _ in range(3)]


while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
