import requests
import threading
import os
import time

class ThreadDownloader:
    
    def __init__(self, img_urls: list) -> None:
        self.__urls = img_urls
        self.__start_time = 0

    def run(self):
        threads = []
        self.__start_time = time.time()

        for url in self.__urls:
            thread = threading.Thread(target=self.__get_img, args=[url])
            threads.append(thread)
            thread.start()
            
        for thread in threads:
            thread.join()

    def __get_img(self, url: str):
        response = requests.get(url=url)
        img_name = 'threading_' + url.split('/')[-1]
        path = os.path.join('images', img_name)
        with open(path, "wb") as f:
            f.write(response.content)
        print(f"Downloaded by threading {url} in {time.time() - self.__start_time:.2f} seconds")
