import glob
from pathlib import Path
import os
import shutil
# print('start')
# list_of_files = glob.glob('/var/www/html/core/static/media/*.svg')  # * means all if need specific format then *.csv
# latest_file = max(list_of_files, key=os.path.getctime)
# print(latest_file)
# print('finish')
DOWNLOAD_DIR = Path(__file__).resolve().parent.parent.joinpath('static/media')
print(DOWNLOAD_DIR)
'/var/www/html/core/static/media'
'/var/www/html/core/bot/static/media'

shutil.move()