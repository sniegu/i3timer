#!/usr/bin/env python3

import argparse
from i3timer import utils

def run():
    parser = argparse.ArgumentParser('i3timer', description='a modern timer')
    parser.add_argument('-d', '--daemon', dest='daemon', default=False, action='store_true')

    parser.add_argument('-s', '--start', dest='action', default=None, action='store_const', const='start')
    parser.add_argument('-t', '--stop', dest='action', default=None, action='store_const', const='stop')
    parser.add_argument('-p', '--pause', dest='action', default=None, action='store_const', const='pause')
    parser.add_argument('-g', '--toggle', dest='action', default=None, action='store_const', const='toggle')

    parser.add_argument('-e', '--shell', dest='shell', default=False, action='store_true')
    parser.add_argument('-c', '--current', dest='current', default=False, action='store_true')

    args = parser.parse_args()


    if args.daemon:
        utils.listen_forever()
    else:
        client = utils.TimerClient()

        if args.shell:
            from IPython import embed
            embed()

        if args.current:
            print(client.state['current'])

        if args.action is not None:
            client.execute(args.action)


