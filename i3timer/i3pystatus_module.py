from i3pystatus import IntervalModule
from i3pystatus.core.util import convert_position
import requests
from i3timer import utils
import solarized
from datetime import timedelta

class TimerModule(IntervalModule):

    settings = (
        ("missing_color", "missing color"),
        ("running_color", "running color"),
        ("paused_color", "paused color"),
    )

    _status = None
    missing_color = '#ff0000'
    running_color = '#00ff00'
    paused_color = '#888888'


    def init(self):
        self.client = utils.TimerClient()

    def run(self):
        try:
            state = self.client.state
            if state['current'] is not None:
                self._status = [{
                    'full_text': str(timedelta(seconds=int(state['current'].total_seconds()))),
                    'color': self.running_color if state['running'] is not None else self.paused_color,
                }]
            else:
                self._status = []

        except Exception as e:
            self._status = [{ 'full_text': 'timer: %s' % e, 'color': self.missing_color }]

    def inject(self, json):
        if self._status:
            for s in self._status:
                json.insert(convert_position(0, json), s)

