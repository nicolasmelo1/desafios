import requests
import bs4


class MrCrawley:
    def __init__(self, base_url=None, header=None):
        self.base_url = base_url if base_url else 'https://old.reddit.com/'
        self.header = header if header else {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:64.0) Gecko/20100101 Firefox/64.0'
        }

    def extract_data(self, subreddit, minimum_score):
        """
        Extracts data from the first page of reddit or subreddit and append it to a list
        If subreddit is 'reddit_home' retrieve threads from reddit home page
        :param subreddit: str
        :param minimum_score: int
        :return: list of dicts - containing threads of specified subreddit
        """

        results = list()
        url = self.base_url if subreddit == 'reddit_home' else self.base_url+'r/'+subreddit
        html = requests.get(url, headers=self.header).content
        soup = bs4.BeautifulSoup(html, 'lxml')

        contents_container = soup.find('div', class_='sitetable')
        contents = contents_container.find_all('div', class_='thing')
        for content in contents:
            try:
                if int(content.find('div', class_='score unvoted')['title']) > minimum_score:
                    result = {
                        'title': content.find('a', {'data-event-action': 'title'}).text,
                        'upvotes': content.find('div', class_='score unvoted')['title'],
                        'subreddit': content['data-subreddit'],
                        'comments': content.find('a', {'data-event-action': 'comments'})['href'],
                        'thread': self.base_url + content['data-permalink']
                    }
                    results.append(result)
            except Exception as e:
                continue

        return results

    def mine(self, text, minimum_score):
        """
        Call this function to crawl through many subreddits and retrieve the results as text
        :param text: str (options separeted by ';')
        :param minimum_score: int (default 5000)
        :return: str - text containing all threads from all subreddits
        """

        subreddits = text.split(';')
        response = ''
        result = '''
Titúlo: {0}
Upvotes: {1}
Subreddit: {2}
Comentários: {3}
Thread: {4}
    '''
        for subreddit in subreddits:
            crawler_response = self.extract_data(subreddit, minimum_score)
            for data in crawler_response:
                response = response + result.format(data['title'], data['upvotes'], data['subreddit'], data['comments'],
                                                    data['thread'])
        return response
