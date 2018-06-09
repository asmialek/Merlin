from body_parts.body import Body
from local.my_place import draw_home


class MerlinObject(object):
    """
    Todo:
        - A parent object for all classes.
        - Wrapper for `test_item()`, with error handling

    """
    pass


if __name__ == "__main__":
    # voice = True
    voice = False
    home = draw_home()
    Merlin = Body(voice=voice, home=home)
    # Merlin.head.brain.test_system()
    while True:
        Merlin.head.think()
