import time
import requests
from bs4 import BeautifulSoup

def fetch(session, url):
    with requests.get(url) as response:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        cont_thumb = soup.findAll('div', 'cont_thumb')
        # print(cont_thumb)
        for cont in cont_thumb:
            title = cont.find('p', 'txt_thumb')
            if title is not None:
                print(title.text)


def main():
    BASE_URL = 'https://bjpublic.tistory.com/category/%EC%A0%84%EC%B2%B4%20%EC%B6%9C%EA%B0%84%20%EB%8F%84%EC%84%9C'
    urls = [f"{BASE_URL}?page={i}" for i in range(1, 10)]
    with requests.Session() as session:
        for url in urls:
            results = fetch(session, url)
            print(results)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end - start)