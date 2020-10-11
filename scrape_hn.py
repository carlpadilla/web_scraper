import requests
from bs4 import BeautifulSoup
import pprint

urls = ['https://news.ycombinator.com/news', 'https://news.ycombinator.com/news?p=2']  # get the first 2 pages
num_page = 0  # counter for the page you are currently in

for url in urls:  # loops through or list of urls and repeats the process :)
    num_page += 1
    res = requests.get(url)
    BeautifulSoup(res.text, 'html.parser')
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.storylink')
    subtext = soup.select('.subtext')


    def sort_stories_by_votes(hnlist):
        return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


    def create_custom_hn(link, subtext):
        hn = []
        for idx, item in enumerate(link):
            title = item.getText()
            href = item.get('href', None)
            vote = subtext[idx].select('.score')
            if len(vote):
                points = int(vote[0].getText().replace(' points', ''))
                if points > 99:
                    hn.append({'title': title, 'link': href, 'votes': points})
        return sort_stories_by_votes(hn)


    print(f' ***Currently on page num: {num_page} ***')  # print num_page
    pprint.pprint(create_custom_hn(links, subtext))