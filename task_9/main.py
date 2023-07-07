import argparse
import asyncio
from multiprocessing import Process
import time
from img_urls import img_urls
from ThreadDowloader import ThreadDownloader
from MultProcDownloader import MultProcDownloader
from AsyncDownloader import AsyncDownloader

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parse image links')
    parser.add_argument('image_links', metavar='S', type=str, nargs='*', help='enter some image links')
    args = parser.parse_args()

    urls = img_urls if len(args.image_links) == 0 else args.image_links

    while(True):
        print('\n\tImage upload menu:')
        print('\nThreading method - enter 1\nMultiprocessing method - enter 2\nAsync method - enter 3')
        print('or enter any different symbol to exit program.')
        choice = input()

        if choice =='1':
            downloader = ThreadDownloader(img_urls=urls)
            downloader.run()
        elif choice == '2': # Пришлось вынести циклы из класса наружу. Т.к. мультипроцессинг не хочет работать не из под main
            processes = []
            start_time = time.time()
            downloader = MultProcDownloader()
                
            for url in urls:
                process = Process(target=downloader.get_img, args=(url, start_time,))
                processes.append(process)
                process.start()
                
            for process in processes:
                process.join()
                
        elif choice == '3':
            downloader = AsyncDownloader(img_urls=urls)
            asyncio.run(downloader.main())
        else:
            exit()

