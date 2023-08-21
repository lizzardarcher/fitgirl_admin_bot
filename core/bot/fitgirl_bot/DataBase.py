import sqlite3 as sql
import traceback
from sqlite3 import Error as SqlError

from settings import DATA_BASE


class DataBase:

    @staticmethod
    def set_new_user(values: tuple) -> None:
        try:
            con = sql.connect(DATA_BASE, check_same_thread=False, timeout=100)
            cur = con.cursor()
            cur.execute('INSERT INTO bot_user VALUES (?,?,?,?,?,?)', values)
            con.commit()
            con.close()
        except:
            print(traceback.format_exc())

    @staticmethod
    def set_logging(values: tuple) -> None:
        try:
            con = sql.connect(DATA_BASE, check_same_thread=False, timeout=100)
            cur = con.cursor()
            cur.execute('INSERT INTO bot_logging (user_id, entry, date) VALUES (?,?,?)', values)
            con.commit()
            con.close()
        except:
            print(traceback.format_exc())

    @staticmethod
    def set_new_game(val: tuple) -> None:
        try:
            with sql.connect(DATA_BASE, check_same_thread=False, timeout=100) as con:
                cur = con.cursor()
                cur.execute('INSERT INTO bot_game (title, image, genre, description, company, languages, '
                            'original_size, repack_size, torrent_link_1337x, torrent_link_magnet, '
                            'torrent_link, torrent_file) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', val)
                con.commit()
        except SqlError:
            print(traceback.format_exc())


    @staticmethod
    def get_game_by_title(val):
        try:
            data_list = []
            with sql.connect(DATA_BASE, check_same_thread=False, timeout=100) as con:
                cur = con.cursor()
                data = cur.execute('SELECT title, image, company, languages, original_size, '
                                   'repack_size, torrent_link_1337x, torrent_link, torrent_file '
                                   'FROM bot_game WHERE title LIKE ?', ('%' + str(val) + '%',)).fetchall()
                for d in data:
                    r = {
                        'title': d[0],
                        'image': d[1],
                        'company': d[2],
                        'languages': d[3],
                        'original_size': d[4],
                        'repack_size': d[5],
                        'torrent_link_1337x': d[6],
                        'torrent_link': d[7],
                        'torrent_file': d[8],
                    }
                    data_list.append(r)
        except SqlError:
            print(traceback.format_exc())
        return data_list
