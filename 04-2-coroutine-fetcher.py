import os
import time
import requests
import aiohttp
import asyncio
import threading

async def fetcher(session, url):
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    async with session.get(url) as response:
        return await response.text()


async def main():
    urls = ['https://google.com', 'https://apple.com'] * 10

    async with aiohttp.ClientSession() as session:
        # result = [fetcher(session, url) for url in urls]
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        print(result)

    # session = requests.Session()
    # session.get(url)
    # session.close()
    

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)