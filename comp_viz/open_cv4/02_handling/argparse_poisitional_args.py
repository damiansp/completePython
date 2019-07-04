import argparse


parser = argparse.ArgumentParser()
parser.add_argument('first_argument', help='his is the first-arg text')
args = parser.parse_args()
print(args.first_argument)
