import logging
import serial
import time


class ArduinoController(object):
    def __init__(self, port, baudrate, name=None,
                 parity=None, prompt='#', termination='\n',
                 timeout=3):
        self.logger = logging.getLogger(name)
        self.serial = serial.Serial()

        self.name = name
        self.serial.port = port
        self.serial.baudrate = baudrate
        if parity:
            self.serial.parity = parity
        self.prompt = prompt
        self.termination = termination
        self.timeout = timeout

        self.serial.open()
        self.query(expected_rtr='Connection made.')
        self.test_item()

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

    def write(self, cmd):
        cmd = self.prompt + str(cmd) + self.termination
        self.logger.debug('Writing: ' + str(cmd.encode('utf-8')))
        self.serial.write(cmd.encode('utf-8'))

    def read(self, timeout=None):
        if timeout is None:
            timeout = self.timeout
        rtr = self.serial.readline()[:-1].decode()
        start_time = time.time()
        while not rtr:
            rtr = self.serial.readline()[:-1].decode()
            time.sleep(0.1)
            if time.time() - start_time > timeout:
                raise ConnectionError('Timeout during read.')
        return rtr

    def query(self, cmd='', expected_rtr='', timeout=None):
        if timeout is None:
            timeout = self.timeout

        if cmd:
            self.write(cmd)
        arduino_rtr = self.read()

        if expected_rtr:
            start_time = time.time()
            while expected_rtr not in arduino_rtr:
                if cmd:
                    self.write(cmd)
                arduino_rtr = self.read()
                time.sleep(0.1)
                if time.time() - start_time > timeout:
                    self.logger.error(f'Excepted \'{expected_rtr}\', '
                                      f'got \'{arduino_rtr}\'!')
                    raise ConnectionError('Query failed.')
        return arduino_rtr

    def test_item(self):
        self.query('aa', 'LED on.')
        self.query('ab', 'LED off.')


if __name__ == '__main__':
    syn = ArduinoController('COM5', 9600)
    # syn.open()
    while True:
        text = input('> ')
        syn.write(text)
