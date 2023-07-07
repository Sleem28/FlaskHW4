import requests
import threading
import os
from url_list import url_list


def save_site(url) -> None:
    response = requests.get(url=url)
    filename = 'threading_' + url.replace('https://','').replace('.', '_').replace('/', '') + '.html'
    path = os.path.join('task_8', 'sites', filename)
    with open(path, "w", encoding='utf-8') as f:
        f.write(response.text)

threads = []

for url in url_list:
    thread = threading.Thread(target=save_site, args=[url])
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()