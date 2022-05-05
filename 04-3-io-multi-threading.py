import os
import time
import requests
import threading
from concurrent.futures import ThreadPoolExecutor

def fetcher(params):
    session = params[0]
    url = params[1]
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with requests.get(url) as response:
        return response.text


def main():
    urls = ['https://google.com', 'https://apple.com'] * 10

    executor = ThreadPoolExecutor(max_workers=10)
    with requests.Session() as session:
        # result = [fetcher(session, url) for url in urls]
        # print(result)
        params = [(session, url) for url in urls]
        results = list(executor.map(fetcher, params))
        print(results)

    # session = requests.Session()
    # session.get(url)
    # session.close()
    

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end - start)