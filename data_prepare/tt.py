# coding=utf-8
import json
import sys
import re
import sqlite3
from sentiment_intensity.STP.test import read_data

reload(sys)
sys.setdefaultencoding("utf-8")

# jso = '{"error": "0","data": [{"name": "1","value": [{"name": "2","value": "3"},{"name": "4","value": "5"}]},{"name": "6","value": [{"name": "7","value": "8"},{"name": "9","value": "10"}]}]}'
jso = '{"content": "。自去年11月份从浦发换到兴业，又一路买进，虽然在兴业上总体盈利，但兴业现在依然低于去年底的收盘价（16.46），希望兴业今年还会再让我惊喜。//", "quote": {"content": ":今天2个账户共中了中影3个签！今年第4次中签，与你同贺！", "reply": "@文之道", "reverted": "@文之道"}}'
db_path = '/Volumes/Macintosh/dataset/stock_sentiment/discussclear.db'

contents = []

def hJson(json_file, i=0):
    # type: (object, object) -> object
    # 判断传入的是否是json对象，不是json对象就返回异常
    if isinstance(json_file, dict):
        for key in json_file.keys():
            key_value = json_file.get(key)
            if isinstance(key_value, dict):
                hJson(key_value, i+1)
            elif isinstance(key_value, list):
                for json_array in key_value:
                    hJson(json_array, i+1)
            else:
                contents.append((str(key)+'_'+str(i), str(key_value)))
    elif isinstance(json_file, list):
        for json_array in json_file:
            hJson(json_array, i+1)
    return contents

comments = json.loads(jso.decode('utf-8'))
print comments
a = read_data.jsonFile()
comment_list = a.hJson(comments)
# comment_list = read_data.jsonFile.hJson(comments)
# comment_list = hJson(comments)

print comment_list
contents = []

