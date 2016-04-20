#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session
import lxml.html
import requests
import re 
def get_birthday(screen_name):
	target_url = "https://twitter.com/" + screen_name
	target_html = requests.get(target_url).text

	root = lxml.html.fromstring(target_html)
	birth_text = root.cssselect(".ProfileHeaderCard-birthdateText")[0].text_content()

	if birth_text.split()==[]:
		return "not set"
	else:
		ret = ""
		match = re.findall(r"\d\d|\d", birth_text)
		for m in match:
			ret += str(m) + "/"
		return ret.rstrip("/")

screen_name = "@shh_y"



CK = 'mDrMIeicXo4ZoBOEZWFbStsA4'                             # Consumer Key
CS = 'Q36qnSugdCLo1K5OJdMof91ekpfF9grnmVccffrHfhH4UEFQBg'         # Consumer Secret
AT = '594426578-SE3o6MCElN09MbgFDEkLjvENG8hKp7aD7WcIhMaU' # Access Token
AS = '3CCOLiDuHQgx9kXMqqg03O0uLmuti3oAblyWuHgfd9mBt'         # Accesss Token Secert

# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"

# ツイート本文
tweet_body = screen_name + "の誕生日は" + get_birthday(screen_name) + "ですね"
params = {"status": tweet_body}

# OAuth認証で POST method で投稿
twitter = OAuth1Session(CK, CS, AT, AS)
req = twitter.post(url, params = params)

# レスポンスを確認
if req.status_code == 200:
    print ("OK") 
else:
    print ("Error: %d" % req.status_code)

