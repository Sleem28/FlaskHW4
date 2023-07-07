import asyncio
import aiohttp
import os
from url_list import url_list

async def save_site(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            site = await response.text()
            filename = 'async_' + url.replace('https://','').replace('.', '_').replace('/', '') + '.html'
            path = os.path.join('task_8', 'sites', filename)
            with open(path, "w", encoding='utf-8') as f:
                f.write(site)

async def main():
    tasks = []

    for url in url_list:
        task = asyncio.create_task(save_site(url))
        tasks.append(task)
    
    for task in tasks:
        await task

if __name__ == '__main__':
    asyncio.run(main())