"""Download latest youtube video"""

import os
import argparse
import downloader
import jsonloader
import player
import youtube_webdriver

build_location = os.path.join(os.getcwd(), 'build', '')
if not os.path.exists(build_location):
    os.makedirs(build_location)

def update_urls():
    "Retrive a list of updated youtube urls"
    start_url = "https://www.youtube.com/watch?v=ru0K8uYEZWw"
    urls = youtube_webdriver.youtube_navigate(start_url)
    jsonloader.serialize(urls, os.path.join(build_location, 'urls.json'), True)


def fetch():
    "Fetch and download those urls"
    urls = jsonloader.deserialize(os.path.join(build_location, 'urls.json'))
    downloader.download(build_location, urls)


def play():
    "Play downloaded all mp3"
    urls = jsonloader.deserialize(os.path.join(build_location, 'urls.json'))
    file_names = [''.join([url.split('watch?v=')[1], ".mp3"]) for url in urls]
    file_paths = [os.path.join(build_location, file_name) for file_name in file_names]
    # print(file_paths)
    player.playAll(file_paths)
    input("Press key to stop")


def main():
    "Main"
    parser = argparse.ArgumentParser(description='Youtube auto downloader and player')
    parser.add_argument(
        '-u', "--update",
        help='retrive a list of updated youtube urls',
        action='store_true')
    parser.add_argument(
        '-f', '--fetch',
        help='fetch and download urls in urls.json',
        action='store_true')

    args = parser.parse_args()
    if args.update:
        update_urls()
        return
    if args.fetch:
        fetch()
        return
    play()


if __name__ == '__main__':
    main()
