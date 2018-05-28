class RCOutlet(object):
    def __init__(self, name, group, id_number, controller):
        self.name = name
        self.group = group
        self.id_number = id_number
        self.controller = controller
        self.is_on = False

    def power(self, state=False):
        if state:
            self.controller.write('')
