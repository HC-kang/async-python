import os
import time
import requests
import threading

def fetcher(session, url):
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with requests.get(url) as response:
        return response.text


def main():
    urls = ['https://google.com', 'https://apple.com'] * 10

    with requests.Session() as session:
        result = [fetcher(session, url) for url in urls]
        print(result)

    # session = requests.Session()
    # session.get(url)
    # session.close()
    

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end - start)