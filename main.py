import argparse
from caesar import caesar
from morse import morse


parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="File to be read")
parser.add_argument("result_file", help="File to save result")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-e', action="store_const", const="e", help="Encrytpion")
group.add_argument('-d', action="store_const", const="d", help="Decryption")
code_group = parser.add_mutually_exclusive_group(required=True)
code_group.add_argument("-m", action="store_const", const="m", help="Use Morse code")
code_group.add_argument("-c", action="store_const", const="c", help="Use Caesar cipher")
parser.add_argument("-n", type=int, default=3, help="Shift in Caesar cipher (If Morse code was chosen this parameter is ignored)")

args = parser.parse_args()

if args.e:
    what="e"
else:
    what="d"

if args.c:
    caesar(args.input_file, args.result_file, what, args.n)

if args.m:
    morse(args.input_file, args.result_file, what)
