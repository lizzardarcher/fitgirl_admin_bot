import os
import shutil
import traceback
import requests
import glob
from time import sleep

from pathlib import Path
from telebot import TeleBot
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

import markup
from selenium_webdriver import get_webdriver_nt
from file_waiter import FileWaiter
from DataBase import DataBase
from settings import TOKEN, DOWNLOAD_MEDIA_DIR, CHANNEL_LIST

bot = TeleBot(TOKEN)
MEDIA_ROOT = str(DOWNLOAD_MEDIA_DIR)

def get_soup(url) -> BeautifulSoup:
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    return soup


def get_info(soup: BeautifulSoup):
    articles = soup.find_all('article')
    for article in articles:
        games = DataBase.get_game_by_title(article.text.lower())
        if not 'upcoming repacks' in article.text.lower() and not games:
            try:
                sleep(5)
                title = article.header.h1.text
                print(str(title).encode('utf-8'))
                image_url = article.find('img')['src']
                image = article.find('img')['src'].split("/")[-1]
                sleep(5)
                # print(image)
                response = requests.get(image_url, stream=True)
                with open(str(Path(DOWNLOAD_MEDIA_DIR).joinpath(image)), 'wb') as out_file:
                    shutil.copyfileobj(response.raw, out_file)
                sleep(5)
                del response
                sleep(1)
                # Fat description
                description = article.find("div", class_='su-spoiler-content').text
                _strong = article.find_all('strong')
                tag = _strong[1].text  # Genre
                # print(tag)
                company = _strong[2].text  # Company
                # print(company)
                languages = _strong[3].text  # Lang
                # print(languages)
                original_size = _strong[4].text  # Gb on disk
                # print(original_size)
                repack_size = _strong[5].text  # Gb torrent
                # print(repack_size)
                torrent_link_1337x = article.find_all('li')[0].a['href']
                # print(torrent_link_1337x)
                torrent_link_magnet = article.find_all('li')[0].findNext('a').findNext('a')['href']
                # print(torrent_link_magnet)
                torrent_link = article.find_all('li')[0].findNext('a').findNext('a').findNext('a')['href']
                # print(torrent_link)
                driver = get_webdriver_nt()
                sleep(1)
                driver.get(url=torrent_link)
                sleep(5)
                a = driver.find_element(By.XPATH, '/html/body/main/section[1]/div[2]/a')
                a.click()
                sleep(5)
                list_of_files = glob.glob(
                    '/root/Downloads/*.torrent')  # * means all if need specific format then *.torrent
                try:
                    latest_file = max(list_of_files, key=os.path.getctime)
                    shutil.move(latest_file, DOWNLOAD_MEDIA_DIR)
                except:
                    latest_file = 'unknown.torrent'
                torrent_file = str(latest_file).split('/')[-1]
                # print('*** *** *** *** *** *** ***')
                # print('torrent_file', torrent_file)
                # print(a)
                try:
                    if not DataBase.get_game_by_title(title):
                        val = (title, image, tag, description, company, languages, original_size, repack_size,
                               torrent_link_1337x, torrent_link_magnet, torrent_link, torrent_file)
                        DataBase.set_new_game(val=val)
                        sleep(1)
                        _message = f'🔶 <b>{title}</b>' + \
                                   f'\n👨🏼‍💻 Разработчик: <code>{company}</code>' + \
                                   f'\n🌏 Язык: <code>{languages}</code>' + \
                                   f'\n🗄 Размер на диске: <code>{original_size}</code>' + \
                                   f'\n🗃 Размер репака: <code>{repack_size}</code>\n'

                        for chat in CHANNEL_LIST:
                            try:
                                bot.send_photo(chat, photo=open(MEDIA_ROOT+'/'+image, 'rb'), caption=_message,
                                               parse_mode='HTML', reply_markup=markup.gen_message_links())
                            except Exception as e:
                                print('Exception Occurred:', e)
                except Exception as e:
                    print('Exception Occurred:', e)
                driver.close()
                sleep(1)
                driver.quit()
                sleep(1)
            except Exception as e:
                print('Exception Occurred:', e)


if __name__ == '__main__':
    # # while True:
    # for page in range(1, 390):
    #     try:
    #         print('Page:', page)
    #         get_info(get_soup(f'https://fitgirl-repacks.site/page/{page}/'))
    #     except: print(traceback.format_exc())
    #     # sleep(86400)
    while True:
        try:
            get_info(get_soup(f'https://fitgirl-repacks.site/page/{1}/'))
        except: print(traceback.format_exc())
        sleep(86400)
