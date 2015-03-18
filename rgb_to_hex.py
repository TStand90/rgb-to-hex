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

        hex_string = "#%02x%02x%02x".upper() % (rgb_red, rgb_green, rgb_blue)

        print(hex_string)


if __name__ == '__main__':
    main()
