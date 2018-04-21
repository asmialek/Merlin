import serial
import time


class ArduinoController(object):
    def __init__(self, port, baudrate, name=None,
                 parity=None, prompt='#', termination='\n',
                 timeout=3):
        self.name = name
        self.serial = serial.Serial()

        self.serial.port = port
        self.serial.baudrate = baudrate
        if parity: self.serial.parity = parity
        self.prompt = prompt
        self.termination = termination
        self.timeout = timeout

    def __del__(self):
        self.serial.close()

    @property
    def status(self):
        """

        Returns:
            bool: Whether communication is opened or not.
        """
        return self.serial.isOpen()

    def open(self):
        self.serial.open()

    def close(self):
        self.serial.close()

    def write(self, data):
        data = self.prompt + str(data) + self.termination
        self.serial.write(data.encode('utf-8'))

    def read(self, timeout=None):
        if timeout is None:
            timeout = self.timeout
        # rtr = self.serial.read()
        rtr = self.serial.readline()[:-1].decode()
        return rtr


if __name__ == '__main__':
    syn = ArduinoController('COM5', 9600)
    syn.open()
    while True:
        syn.write(input())
        # print(syn.read())
    # print(syn.status)
