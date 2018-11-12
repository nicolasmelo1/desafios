from argparse import ArgumentParser
from mr_crawley import MrCrawley


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--mine', type=str.lower, action='store',
                        help="insert each option divided by ';' to retrieve data",
                        required=False)
    parser.add_argument('--telegram', action='store_true')
    args = parser.parse_args()

    if args:
        if args.telegram:
            pass
        crawler = MrCrawley()
        subreddits = args.mine.split(';')

        print_result = '''
Title: {0}
Upvotes: {1}
Subreddit: {2}
Comments: {3}
Thread: {4}
        '''
        for subreddit in subreddits:
            response = crawler.whats_poppin(subreddit)
            for data in response:
                print(print_result.format(data['title'], data['upvotes'], data['subreddit'], data['comments'], data['thread']))

