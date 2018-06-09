from physicals.room import Room
from physicals.instruments.arduino import Arduino
import logging


class Home(object):
    def __init__(self, name):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.name = name
        self.rooms = []
        self.room_groups = ['living_room',
                            'bathroom',
                            'bedroom',
                            'kitchen',
                            ]
        self.controllers = []

    def add_rooms(self, *rooms):
        for room in rooms:
            self._add_room(room)

    def _add_room(self, room_obj):
        """

        Todo:
            Add name check.

        Args:
            room_obj:

        """
        if not isinstance(room_obj, Room):
            raise TypeError('Object is not of \'Room\' class.')
        if room_obj.group not in self.room_groups:
            raise NotImplementedError(f'Name \'{room_obj.group}\' is '
                                      f'not a valid room group name!')
        room_obj.home = self
        self.rooms.append(room_obj)
        self.logger.debug(f'Room \'{room_obj.name}\' added to '
                          f'\'{self.name}\'.')

    def add_controllers(self, *controllers):
        for controller in controllers:
            self._add_controller(controller)

    def _add_controller(self, controller_obj):
        """

        Todo:
            Add name check.

        Args:
            controller_obj:

        """
        if not isinstance(controller_obj, Arduino):
            raise TypeError('Object is not of \'Arduino\' class.')
        controller_obj.home = self
        self.controllers.append(controller_obj)

    def test_item(self):
        for controller in self.controllers:
            controller.test_item()
        for room in self.rooms:
            room.test_item()
