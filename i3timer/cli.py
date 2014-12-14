#!/usr/bin/env python3

import argparse
from i3timer import utils

parser = argparse.ArgumentParser('i3timer', description='a modern timer')
parser.add_argument('-d', '--daemon', dest='daemon', default=False, action='store_true')
parser.add_argument('-s', '--start', dest='action', default=None, action='store_const', const='start')
parser.add_argument('-t', '--stop', dest='action', default=None, action='store_const', const='stop')
parser.add_argument('-p', '--pause', dest='action', default=None, action='store_const', const='pause')
parser.add_argument('-c', '--current', dest='action', default=None, action='store_const', const='current')
parser.add_argument('-e', '--shell', dest='action', default=None, action='store_const', const='shell')

args = parser.parse_args()

if args.daemon:

    utils.listen_forever()

if args.action is not None:

    client = utils.TimerClient()

    if args.action == 'current':
        print(client.state['current'])

    if args.action == 'start':
        client.execute('start')

    if args.action == 'stop':
        client.execute('stop')

    if args.action == 'pause':
        client.execute('pause')

    if args.action == 'shell':
        from IPython import embed ; embed()

