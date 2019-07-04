import argparse


parser = argparse.ArgumentParser()
parser.add_argument('n1', help='first number', type=int)
parser.add_argument('n2', help='second number', type=int)
args = parser.parse_args()
print(f'args: {args}')
print(f'sum: {args.n1 + args.n2}')
args_dict = vars(args)
for k, v in args_dict.items():
    print(f'{k}: {v}')
print(f'2nd arg: {args_dict["n2"]}')
