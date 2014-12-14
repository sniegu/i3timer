# coding=utf-8
from multiprocessing.connection import Listener, Client
from os import path
import datetime

address = path.expanduser('~/.i3timer/pipe')
authkey = b'i3timer'


class Timer(object):

    def __init__(self):
        self.stop()

    @property
    def current(self):
        if self.accumulator is None:
            return self.running

        r = self.running
        if r is None:
            return self.accumulator
        else:
            return self.accumulator + r

    @property
    def running(self):
        return datetime.datetime.now() - self.last_start if self.last_start is not None else None

    def get_state(self):
        return {'current': self.current, 'running': self.running}

    def start(self):
        self.last_start = datetime.datetime.now()

    def pause(self):
        self.accumulator = self.current
        self.last_start = None

    def stop(self):
        self.last_start = None
        self.accumulator = None


def listen_forever():

    timer = Timer()

    with Listener(address=address, authkey=authkey) as listener:
        while True:
            conn = listener.accept()
            try:
                message = conn.recv()
                conn.send(getattr(timer, message)())
                conn.close()
            except EOFError as e:
                pass
            except Exception as e:
                print('exception occurred: %s' % e)


class TimerClient(object):

    def __init__(self):
        pass

    def execute(self, command):
        client = Client(address=address, authkey=authkey)
        client.send(command)
        return client.recv()

    @property
    def state(self):
        return self.execute('get_state')







