import argparse
import sys
from . import converters


def parse_args(argv):
    parser = argparse.ArgumentParser(
        prog='fun_with_unicode',
        description='Do off-the-wall things with Unicode characters and strings.'
    )
    parser.add_argument(
        '-x',
        '--to-codes',
        action='store_true',
        help="Convert input to Unicode character codes",
    )
    parser.add_argument(
        '-s',
        '--to-string',
        action='store_true',
        help="Convert input to Unicode string",
    )
    parser.add_argument(
        'input',
        type=str,
        help='Input values',
        nargs='?',
    )
    return parser.parse_args(argv), parser
    
    
def do_to_codes(input):
    def do_conversion(input_str):
        return "--> %s <--" % ' '.join(f'{i:x}' for i in converters.string_to_codes(input_str.strip()))
    if input is not None:
        print(do_conversion(input))
        sys.exit(0)
    for line in sys.stdin:
        if len(line.strip()) == 0:
            sys.exit(0)
        print(do_conversion(line))


def do_to_string(input):
    def do_conversion(input_str):
        codes = [int(s, 16) for s in input_str.split()]
        return "--> %s <--" % converters.codes_to_string(codes)
    if input is not None:
        print(do_conversion(input))
        sys.exit(0)
    for line in sys.stdin:
        if len(line.strip()) == 0:
            sys.exit(0)
        print(do_conversion(line))


def main(args, print_help):
    if args.to_codes:
        do_to_codes(args.input)
        sys.exit(0)
    if args.to_string:
        do_to_string(args.input)
        sys.exit(0)
    print_help()
    sys.exit(1)

if __name__ == "__main__":
    args, parser = parse_args(sys.argv[1:])
    main(args, parser.print_help)