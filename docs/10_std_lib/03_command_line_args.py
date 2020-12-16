# Run as, e.g.,
# > python3 03_command_line_args.py --lines=5 garbage trash
import argparse
import sys


print(sys.argv)

parser = argparse.ArgumentParser(prog='03_command_line_args',
                                 description='Show top lines from each file')
parser.add_argument('filename', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=5)
args = parser.parse_args()
print(args)
                                 
