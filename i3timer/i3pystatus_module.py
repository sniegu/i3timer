from i3pystatus import IntervalModule
from i3pystatus.core.util import convert_position
import requests
from i3timer import utils
import solarized
from datetime import timedelta

class TimerModule(IntervalModule):

    # settings = (
    #     ("url", "url to request"),
    #     ("missing_color", "missing color"),
    # )

    # url = 'http://127.0.0.1:9000/api/status'
    # missing_color = '#ff0000'

    _status = None


    def init(self):
        self.client = utils.TimerClient()

    def run(self):
        try:
            state = self.client.state
            if state['current'] is not None:
                self._status = [{
                    'full_text': str(timedelta(seconds=int(state['current'].total_seconds()))),
                    'color': solarized.magenta if state['running'] is not None else solarized.base02,
                }]
            else:
                self._status = []

        except Exception as e:
            self._status = [{ 'full_text': 'timer', 'color': solarized.red }]

    def inject(self, json):
        if self._status:
            for s in self._status:
                json.insert(convert_position(0, json), s)

