import argparse
import argcomplete
from autymatedesigner._version import get_versions


def parse_args(args):
    parser = argparse.ArgumentParser(description='Mindbike mindmapping.\n Execute as follows: main.py -- files')
    parser.add_argument('files', nargs='*', help='The mindmap(s) to load')
    parser.add_argument('--version', help='Get the mindbike version', action='version',
                        version=get_versions()['version'])

    argcomplete.autocomplete(parser)

    return parser.parse_args(args)
