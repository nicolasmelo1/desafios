from argparse import ArgumentParser
from magic_formatter import MagicFormatter

if __name__ == '__main__':
    """
    if you are running from the terminal you can either pass a text as a String
    or a file location, if on the same path just pass the file name.
    
    Also, you need to pass the width of the text you want to format.
    """
    parser = ArgumentParser()
    parser.add_argument('text', type=str, help='insert text, file name or file path')
    parser.add_argument('width', type=int, help='insert width of text')
    args = parser.parse_args()

    if args:
        formatter = MagicFormatter(args.text, args.width)
        formatter.reformat_text('output-parte1.txt')
        formatter.reformat_text('output-parte2.txt', True)
