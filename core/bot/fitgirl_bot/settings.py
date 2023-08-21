from pathlib import Path

DOWNLOAD_TORRENT_DIR = Path(__file__).resolve().parent.joinpath('torrent')
DOWNLOAD_MEDIA_DIR = Path(__file__).resolve().parent.parent.parent.joinpath('static').joinpath('media')
DATA_BASE = Path(__file__).resolve().parent.parent.parent.joinpath('db.sqlite3')
TOKEN = '6203271537:AAGmtF9GO9kLXpaae1GWkacOtzBeYucDC4o'
CHANNEL_LIST = [-1001713921044,]

# print(DOWNLOAD_TORRENT_DIR)
# print(DOWNLOAD_MEDIA_DIR)
# print(DATA_BASE)
