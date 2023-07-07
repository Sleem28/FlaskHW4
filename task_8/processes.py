import requests
from multiprocessing import Process
import os
from url_list import url_list


def save_site(url) -> None:
    response = requests.get(url=url)
    filename = 'proc_' + url.replace('https://','').replace('.', '_').replace('/', '') + '.html'
    path = os.path.join('task_8', 'sites', filename)
    with open(path, "w", encoding='utf-8') as f:
        f.write(response.text)

processes = []

if __name__ == '__main__':
    for url in url_list:
        process = Process(target=save_site, args=(url,))
        processes.append(process)
        process.start()
        
    for process in processes:
        process.join()