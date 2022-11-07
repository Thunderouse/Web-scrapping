import bs4
from fake_headers import Headers
import requests


if __name__ == "__main__":
    KEYWORDS = ['История IT', 'Разработка веб-сайтов *', 'Удалённая работа', 'Python *', 'Программирование *', 'Беспроводные технологии *']
    url = 'https://habr.com/ru/all/'
    habr_headers = Headers(os="mac", headers=True).generate()
    response = requests.get(url=url, headers=habr_headers)
    text = response.text
    soup = bs4.BeautifulSoup(text, features='html.parser')
    articles = soup.find_all("article")
    for article in articles:
        hubs = article.find_all(class_="tm-article-snippet__hubs-item")
        hubs = [hub.text.strip() for hub in hubs]
        for hub in hubs:
            if hub in KEYWORDS:
                href = article.find(class_='tm-article-snippet__title-link').attrs['href']
                title = article.find(class_='tm-article-snippet__title-link').text
                time = article.find(class_='tm-article-snippet__datetime-published').time['datetime']
                full_href = url + href
                print(time, title, full_href)