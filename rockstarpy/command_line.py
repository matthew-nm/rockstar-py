import sys
import argparse

from rockstarpy.convert import convert_line


parser = argparse.ArgumentParser(description="Python transpiler for the esoteric language Rockstar")

input_group = parser.add_mutually_exclusive_group(required=True)
input_group.add_argument('--input', action='store', help='Input file (.rock)')
input_group.add_argument('--stdin', action='store_true', help='Stream in stdin')

output_group = parser.add_mutually_exclusive_group(required=True)
output_group.add_argument('--output', action='store', help='Output file (.py)', default='output.py')
output_group.add_argument('--stdout', action='store_true', help='Stream to stdout')

parser.add_argument('-v', action='version', help='Version', version='1.3.6')

args = parser.parse_args()


def command_line():

    # open I/O
    if args.stdin:
        lyrics = sys.stdin
    else:
        lyrics = open(args.input, 'r')

    if args.stdout:
        output = sys.stdout
    else:
        output = open(args.output, 'wb', 0)

    # Read, Convert, Write (loop)
    for line in lyrics:
        output.write( convert_line(line) if args.stdout
                      else convert_line(line).encode() )

    # close I/O
    if not args.stdin:
        lyrics.close()
    if not args.stdout:
        output.close()
