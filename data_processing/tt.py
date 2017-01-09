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

# jso = '{"error": "0","data": [{"name": "1","value": [{"name": "2","value": "3"},{"name": "4","value": "5"}]},{"name": "6","value": [{"name": "7","value": "8"},{"name": "9","value": "10"}]}]}'
jso = '{"content": "。自去年11月份从浦发换到兴业，又一路买进，虽然在兴业上总体盈利，但兴业现在依然低于去年底的收盘价（16.46），希望兴业今年还会再让我惊喜。//", "quote": {"content": ":今天2个账户共中了中影3个签！今年第4次中签，与你同贺！", "reply": "@文之道", "reverted": "@文之道"}}'
# db_path = '/Volumes/Macintosh/dataset/stock_sentiment/discussclear.db'
db_path = '/Volumes/Macintosh/dataset/stock_sentiment/data.sqlite'
data_cleaning.add_column_sqlite(db_path, 'SH600152', 'test')