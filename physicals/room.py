from physicals.instruments.rc_outlet import RCOutlet


class Room(object):
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.rc_outlets = []
        self.home = None

    def add_outlets(self, *outlets):
        for outlet in outlets:
            self._add_outlet(outlet)

    def _add_outlet(self, outlet_obj):
        if not isinstance(outlet_obj, RCOutlet):
            raise TypeError('Object is not of \'RCOutlet\' class.')
        elif outlet_obj.name in [x.name for x in self.rc_outlets]:
            raise NameError(f'Name {outlet_obj.name} is already in use.')
        elif outlet_obj.id_number in [x.id_number for x in self.rc_outlets]:
            raise AttributeError(f'If {outlet_obj.id_number} is already in '
                                 f'use.')
        elif outlet_obj.controller not in self.home.controllers:
            raise AttributeError(f'Controller \'{outlet_obj.name}\' is not'
                                 f'added to the house.')
        self.rc_outlets.append(outlet_obj)

    def test_item(self):
        for outlet in self.rc_outlets:
            outlet.test_item()
