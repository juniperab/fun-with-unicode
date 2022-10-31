import argparse
import pyperclip
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


def convert_to_codes(input_str):
    result = ' '.join(f'{i:x}' for i in converters.string_to_codes(input_str))
    pyperclip.copy(result)
    return "\t%s" % result
    
    
def convert_to_string(input_str):
    codes = [int(s, 16) for s in input_str.split()]
    result = converters.codes_to_string(codes)
    pyperclip.copy(result)
    return "\t%s" % result

    
# def do_to_codes(input):
#     def do_conversion(input_str):
#         result = ' '.join(f'{i:x}' for i in converters.string_to_codes(input_str.strip()))
#         pyperclip.copy(result)
#         return "\t%s" % result
#     if input is not None:
#         print(do_conversion(input))
#         sys.exit(0)
#     print("Type in characters; press 'enter' to convert. Input a blank line to exit.")
#     for line in sys.stdin:
#         if len(line.strip()) == 0:
#             sys.exit(0)
#         print(do_conversion(line))
#
#
# def do_to_string(input):
#     def do_conversion(input_str):
#         codes = [int(s, 16) for s in input_str.split()]
#         result = converters.codes_to_string(codes)
#         pyperclip.copy(result)
#         return "\t%s" % result
#     if input is not None:
#         print(do_conversion(input))
#         sys.exit(0)
#     print("Type in hex codes, separated by spaces; press 'enter' to convert. Input a blank line to exit.")
#     for line in sys.stdin:
#         if len(line.strip()) == 0:
#             sys.exit(0)
#         print(do_conversion(line))


def main(args, print_help):
    if args.to_codes:
        convert = convert_to_codes
    elif args.to_string:
        convert = convert_to_string
    else:
        print_help()
        sys.exit(1)

    if args.input is not None:
        # Take input from arguments
        print(convert(args.input))
    else:
        # Take input from stdin
        for line in sys.stdin:
            if len(line.strip()) == 0:
                sys.exit(0)
            if line[-1] == '\n':
                line = line[0:-1]
            if not sys.stdin.isatty():
                print(line)
            print(convert(line))
    

if __name__ == "__main__":
    args, parser = parse_args(sys.argv[1:])
    main(args, parser.print_help)
