# fun with unicode

Python functions for doing off-the-wall things with Unicode characters and strings.


### Usage

Convert a single string to code point(s): `python3 -m fun_with_unicode -x '👧🏻'`

Convert a sequence of code points to a strong: `python3 -m fun_with_unicode -s '1f3f4 200d 2620 fe0f'`

Convert multiple strings to code points: `python3 -m fun_with_unicode -x < example_strings.txt`

Convert multiple code point sequences to strings: `python3 -m fun_with_unicode -s < example_codes.txt`

N.B. Results are also copied to the clipboard after each conversion.
