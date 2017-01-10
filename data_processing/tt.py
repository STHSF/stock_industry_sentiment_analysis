# coding=utf-8
import json
import sys
import re
import sqlite3
from sentiment_intensity.STP.test import read_data
from sentiment_intensity.STP import sentiment
import data_cleaning
reload(sys)
sys.setdefaultencoding("utf-8")

db_path = '/Volumes/Macintosh/dataset/stock_sentiment/discussclear.db'
# db_path = '/Volumes/Macintosh/dataset/stock_sentiment/data.sqlite'
# data_cleaning.add_column_sqlite(db_path, 'SH600152', 'test')

print 3 % 2 == 0