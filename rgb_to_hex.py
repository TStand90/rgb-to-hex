import sys
import argparse
import os


def get_rgb_from_file(input_file):
    if os.path.exists(input_file):
        rgb_list = []

        with open(input_file) as f:
            for line in f:
                rgb_list.append(line)

        return rgb_list
    else:
        print("Error: Input file does not exist")
        sys.exit(1)


def get_hex_list(rgb_list):

    hex_list = []

    for eachRGB in rgb_list:
        red, green, blue = eachRGB.split(',')

        rgb_red = int(red)
        rgb_green = int(green)
        rgb_blue = int(blue)

        range_errors = []

        if not number_in_range(rgb_red):
            range_errors.append(red)
        if not number_in_range(rgb_green):
            range_errors.append(green)
        if not number_in_range(rgb_blue):
            range_errors.append(blue)

        if range_errors:
            errors = ', '.join(set(range_errors))
            print("Error: %s not in range 0-255" % errors)
        else:
            hex_string = '#%02x%02x%02x'.upper() % (rgb_red,
                                                    rgb_green,
                                                    rgb_blue)
            hex_list.append(hex_string)

    return hex_list


def number_in_range(number):
    if number in range(256):
        return True
    else:
        return False


def main():

    parser = argparse.ArgumentParser(description='Convert RGB to hexidecimal' +
                                     'representation.')
    parser.add_argument('rgb', metavar='N', nargs='*')
    parser.add_argument('-i', '--input', help='Input file, with each RGB' +
                        'pair new line separated')

    args = parser.parse_args()

    if args.input:
        rgb_pairs = get_rgb_from_file(args.input)
    elif args.rgb:
        rgb_pairs = args.rgb
    else:
        print("Error: Did not receive any arguments.")
        sys.exit(1)

    hex_list = get_hex_list(rgb_pairs)

    for eachHex in hex_list:
        print(eachHex)


if __name__ == '__main__':
    main()
