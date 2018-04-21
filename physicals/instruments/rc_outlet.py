class RCOutlet(object):
    def __init__(self, name, controller, room):
        self.room = room
        self.name = name
        self.controller = controller
        self.is_on = False
