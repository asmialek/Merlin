class RCOutlet(object):
    def __init__(self, name, group, id_number, controller):
        self.name = name
        self.group = group
        self.id_number = id_number
        self.controller = controller
        self.is_on = False

    def power(self, state=False):
        if state:
            state_char = 'a'
        else:
            state_char = 'b'
        msg = 'd' + chr(self.id_number) + state_char
        self.controller.write(msg)

    def test_item(self):
        self.power(True)
        self.power(False)
