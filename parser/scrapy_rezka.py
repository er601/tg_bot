import requests
from bs4 import BeautifulSoup

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
}


URL = "https://rezka.ag/"


def get_requests(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="b-content__inline_item")
    shows = []

    for item in items:
        shows.append(
            {
                "link": item.find("div", class_="b-content__inline_item-cover").find("a").get("href"),
                "img": item.find("div", class_="b-content__inline_item-cover").find("a").find("img").get("src"),
                "title": item.find("div", class_="b-content__inline_item-link").find("a").get_text(),
                "date_": item.find("div", class_="b-content__inline_item-link").find("div").get_text(),
            }
        )
    return shows


def scrapy_script():
    html = get_requests(URL)
    if html.status_code == 200:
        shows = []
        for page in range(1, 3):
            html = get_requests(f'https://rezka.ag/page/{page}')
            shows.extend(get_data(html.text))
        return shows
    else:
        raise Exception("Error in scrapy script function")

