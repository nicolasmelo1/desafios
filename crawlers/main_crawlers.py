from argparse import ArgumentParser
from mr_crawley import MrCrawley
from telegram_bot import TelegramBot


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--set', type=int, action='store', help='set minimum number of upvotes', required=False)
    parser.add_argument('--mine', type=str.lower, action='store',
                        help="insert each option divided by ';' to retrieve data",
                        required=False)
    parser.add_argument('--telegram', action='store_true', help='start telegram bot, all other arguments are ignored, '
                                                                'don\'t need to pass value')
    args = parser.parse_args()

    if args:
        crawler = MrCrawley()
        if args.telegram:
            TelegramBot()
        else:
            print(crawler.mine(args.mine, args.set if args.set else 5000))

