import argparse
from colorize import Colorize

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--source', dest='source', action='store', help='Source folder')
parser.add_argument('-d', '--dest', dest='destination', action='store', help='Destination folder')
args = parser.parse_args()


if __name__ == "__main__":
    Colorize(args)
