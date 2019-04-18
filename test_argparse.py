import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-all', help='run script with all the data sets')
parser.add_argument('-some', help='run script with specified data sets', choices=['MBC', 'ERG', 'TOC'])

args   = parser.parse_args()

if args.all:
    print('all')

else:
    print(args.some)