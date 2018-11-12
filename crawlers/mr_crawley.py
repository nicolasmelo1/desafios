import requests
import bs4


class MrCrawley:
    def __init__(self, base_url=None, header=None):
        self.base_url = base_url if base_url else 'https://old.reddit.com/'
        self.header = header if header else {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:64.0) Gecko/20100101 Firefox/64.0'
        }

    def whats_poppin(self,subreddit):
        results = list()
        url = self.base_url if subreddit is 'reddit_home' else self.base_url+'r/'+subreddit

        html = requests.get(url, headers=self.header).content
        soup = bs4.BeautifulSoup(html, 'lxml')

        contents_container = soup.find('div', class_='sitetable')
        contents = contents_container.find_all('div', class_='thing')

        for content in contents:
            try:
                if int(content.find('div', class_='score unvoted')['title']) > 5000:
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
