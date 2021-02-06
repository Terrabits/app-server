import argparse


def parse():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--host',          default='0.0.0.0')
    parser.add_argument('--port',          default=8080, type=int)
    parser.add_argument('--instr-address', default='localhost')
    parser.add_argument('--instr-port',    default=5025, type=int)
    parser.add_argument('--open-browser',  action='store_true')
    parser.add_argument('directory',       default='.')
    return parser.parse_args()
