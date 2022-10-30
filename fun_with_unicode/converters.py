def codes_to_string(codes):
    return (b'\xff\xfe\x00\x00' + b''.join(c.to_bytes(4, 'little') for c in codes)).decode('utf32')

def string_to_codes(unicode_string):
    all_bytes = unicode_string.encode('utf32')
    split_bytes = [all_bytes[(i+1)*4:(i+2)*4] for i in range(int(len(all_bytes)/4)-1)]
    split_ints = [int.from_bytes(b, 'little', signed=False) for b in split_bytes]
    return split_ints
