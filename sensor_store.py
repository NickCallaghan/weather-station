import sqlite3 as sqlite
from datetime import datetime


class SensorStore:
    def __init__(self, filename):
        self.filename = filename
        try:
            self.con = sqlite.connect(filename)
            self.cur = self.con.cursor()
            query = '''CREATE TABLE IF NOT EXISTS sensor_readings (
                    `reading_id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    `reading_type`	TEXT NOT NULL,
                    `reading_value`	REAL,
                    `reading_dt`	TEXT
            );'''
            self.cur.execute(query)
        except sqlite.Error as e:
            print(f'Error {e.args[0]}')

    def write_sensor_reading(self, reading_value, reading_type):
        try:
            query = f'INSERT INTO sensor_readings VALUES(NULL, ?, ?, ?);'
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y, %H:%M:%S")
            self.cur.execute(query, (reading_type, reading_value, dt_string))
            self.con.commit()

        except sqlite.Error as e:
            print(f'Error {e.args[0]}')

    def close(self):
        self.con.close()
