from physicals.instruments.rc_outlet import RCOutlet


class Room(object):
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.rc_outlets = []