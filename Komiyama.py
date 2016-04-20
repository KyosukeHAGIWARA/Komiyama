#!/usr/bin/env python3
# coding: utf-8

from tweepy.streaming import StreamListener, Stream
from tweepy.auth import OAuthHandler
from tweepy.api import API
from datetime import timedelta, datetime
import sqlite3
import __main__
import threading
import time
import ConfigParser

class SubThread(threading.Thread):

    """docstring for TestThread"""

    def __init__(self, n, t):
        super(SubThread, self).__init__()
        self.n = n
        self.t = t

    def run(self):
        print " === start sub thread (sub class) === "
        for i in range(self.n):
            time.sleep(self.t)
            print "sub thread (sub class) : " + str(datetime.today())
        print " === end sub thread (sub class) === "

count_flg = False

def get_oauth():
    conf = ConfigParser.SafeConfigParser()
    conf.read("twitter.ini")
    auth = OAuthHandler(conf.get("Twitter", "CK"), conf.get("Twitter", "CS"))
    auth.set_access_token(conf.get("Twitter", "AT"), conf.get("Twitter", "AS"))

    return auth

def update_tweet(text):
    auth = get_oauth()
    api = API(auth)
    api.update_status(status=text)

def update_reply(text, reply_id, screen_name):
    auth = get_oauth()
    api = API(auth)
    st = "@" + str(screen_name) + " " + str(text)
    api.update_status(status=st, in_reply_to_status_id=reply_id)

def insert_data(text):
    status_text = text.split(" ")
    connector = sqlite3.connect("sqlite_test1.db")

    sql = "insert into test_table(id, name) values(?,?)"
    connector.execute(sql, (len(text), text))

    connector.commit()
    cursor = connector.cursor()
    cursor.execute("select * from test_table order by id")
 
    result = cursor.fetchall()

    for row in result:
        print "===== Hit! ====="
        print "code -- " + unicode(row[0])
        print "name -- " + unicode(row[1])
    cursor.close()
    connector.close()

def init_database():
    connector = sqlite3.connect("Komiyama.db")
    cursor = connector.cursor()
    sql = "create table if not exists event_table(id integer, title text, ts timestamp, note text, screen_name text )"
    cursor.execute(sql)
    cursor.execute("select * from sqlite_master")
    res = cursor.fetchall()
    for row in res:
        print(row)
    cursor.close()
    connector.close()

def insert_event_data(title, datetime, note, screen_name):
    pass 

#observe user stream
class AbstractedlyListener(StreamListener):
    """ Let's stare abstractedly at the User Streams ! """
    def on_status(self, status):
        status.created_at += timedelta(hours=9)
        recog_status(status)
            

def recog_status(status):
    print("get status")
    text = status.text.encode('utf-8')
    if status.source=="Komiyama":#not reply for app
        print("LOG : detect app's tweet")
    elif "おきてる" in text or "起きてる" in text:
        body = "眠いけどね。"
        update_reply(body, status.id, status.author.screen_name)
    elif "#こみこみconfig" in text:
        if "文字数数えて" in text:
            __main__.count_flg = True
            body = "りょ はじめるわ"
            update_reply(body, status.id, status.author.screen_name)
        elif "うるさい" in text:
            __main__.count_flg = False
            body = "ごめんやめるわ"
            update_reply(body, status.id, status.author.screen_name)
    elif __main__.count_flg:
        body = "それ" + str(len(text)) + "文字"
        update_reply(body, status.id, status.author.screen_name)
    elif "#こみこみTODO" in text:
        q = text.split(" ")
        body = ""
        if len(q)==3:
            body = "\ntitle: " + q[0] + "\n" + "limit: " + q[1] + "\n" + "で登録しとくね"
            insert_event_data(q[0], q[1], "", str(status.author.screen_name))
        elif len(q)==4:
            body = "\ntitle: " + q[0] + "\n" + "limit: " + q[1] + "\n" + "note: " + q[2] + "\n" + "で登録しとくね"
            insert_event_data(q[0], q[1], q[2], str(status.author.screen_name))
        elif len(q)<=2 or len(q)>=5:
            body = " usage\n [title] [limit] [note(optional)] #こみこみTODO\nでおなしゃす"
        update_reply(body, status.id, status.author.screen_name)
    elif "#こみこみANNIV" in text:
        q = text.split(" ")
        body = ""
        if len(q)==3:
            body = "\ntitle: " + q[0] + "\n" + "date: " + q[1] + "\n" + "で登録しとくね"
            insert_event_data(q[0], q[1], "", str(status.author.screen_name))
        elif len(q)==4:
            body = "\ntitle: " + q[0] + "\n" + "date: " + q[1] + "\n" + "note: " + q[2] + "\n" + "で登録しとくね"
            insert_event_data(q[0], q[1], q[2], str(status.author.screen_name))
        elif len(q)<=2 or len(q)>=5:
            body = " usage\n [title] [date] [note(optional)] #こみこみANNIV\nでおなしゃす"
        update_reply(body, status.id, status.author.screen_name)
    else:
        pass


if __name__ == '__main__':
    th_cl = SubThread(5, 10)
    # th_cl.start()
    init_database()
    auth = get_oauth()
    stream = Stream(auth, AbstractedlyListener(), secure=True)
    stream.userstream()

    
