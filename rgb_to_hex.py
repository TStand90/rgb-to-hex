import sys
import argparse


def main():

    parser = argparse.ArgumentParser(description='Convert RGB to hexidecimal' +
                                     'representation.')
    parser.add_argument('rgb', metavar='N', nargs='+')

    args = parser.parse_args()

    for eachArg in args.rgb:
        red, green, blue = eachArg.split(',')

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
            print(hex_string)


def number_in_range(number):
    if number in range(256):
        return True
    else:
        return False


if __name__ == '__main__':
    main()
