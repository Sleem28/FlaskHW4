import asyncio
import aiohttp
import requests
import time
import os

class AsyncDownloader:
    def __init__(self, img_urls: list) -> None:
        self.__urls = img_urls
        self.__start_time = 0

    async def __get_img(self,url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response = requests.get(url=url)
                img_name = 'async_' + url.split('/')[-1]
                path = os.path.join('images', img_name)
                with open(path, "wb") as f:
                    f.write(response.content)
                print(f"Downloaded by async {url} in {time.time() - self.__start_time:.2f} seconds")

    async def main(self):
        tasks = []
        self.__start_time = time.time()

        for url in self.__urls:
            task = asyncio.create_task(self.__get_img(url))
            tasks.append(task)
        
        for task in tasks:
            await task