import requests
from multiprocessing import Process
import os
import time

class MultProcDownloader:

    def get_img(self, url: str, start_time: time):
        response = requests.get(url=url)
        img_name = 'multproc_' + url.split('/')[-1]
        path = os.path.join('images', img_name)
        with open(path, "wb") as f:
            f.write(response.content)
        print(f"Downloaded by multiprocessing {url} in {time.time() - start_time:.2f} seconds")
