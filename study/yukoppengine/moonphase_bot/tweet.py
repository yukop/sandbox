#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os

to_add = os.path.join(os.path.dirname(__file__), "astral")
sys.path.append(to_add)
to_add = os.path.join(os.path.dirname(__file__), "pytz-2012f")
sys.path.append(to_add)

import oauth
import datetime
import pytz
from astral import *

#moonphase_bot
application_key = 'aM6DVHV6mwLC2CJvz5QX4w'
application_secret = '95y9T1QVBgWKsDH23focyvnShnzD5xXkETlG6Hg'
user_token = '879196322-z9jNZyXM32BNz0HV1QXut5KL661NZ5baEfHV9IOP'
user_secret = 'OuLtmEdmNvREEmgzjKo0lmwtJutkiOY2Rd2PViEjCs'

client = oauth.TwitterClient(application_key, application_secret, None)
url = 'https://api.twitter.com/1/statuses/update.json'

a = Astral()
moonphase = a.moon_phase(datetime.datetime.now(), None)
if moonphase == 1:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。新月だよ。"
elif moonphase == 2:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。既朔っていうらしい。"
elif moonphase == 3:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。三日月だね。眉月、蛾眉、繊月ともいうし、たくさんの異名があるよ。crescent もクロワッサンも三日月のことなんだって！"
elif moonphase == 4:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。"
elif moonphase == 5:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。"
elif moonphase == 6:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。"
elif moonphase == 7:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。上弦の月だね。"
elif moonphase == 8:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。"
elif moonphase == 9:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。"
elif moonphase == 10:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。十日夜の月。"
elif moonphase == 11:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。"
elif moonphase == 12:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。"
elif moonphase == 13:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。十三夜月、もうすぐ満月だね。"
elif moonphase == 14:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。小望月！"
elif moonphase == 15:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。満月だよ。"
elif moonphase == 16:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。十六夜。不知夜月ともいうんだって。"
elif moonphase == 17:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。立待月なのでがんばって待とう。"
elif moonphase == 18:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。居待月。昨日は月の出を立って待ったけど、きょうは座って待つんだね。"
elif moonphase == 19:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。寝待月だよ。待ちきれなくてついにねちゃったね。"
elif moonphase == 20:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。更待月は夜更けごろに出てくるらしいよ。"
elif moonphase == 21:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。"
elif moonphase == 22:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。"
elif moonphase == 23:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。下弦の月だねえ。"
elif moonphase == 24:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。"
elif moonphase == 25:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。"
elif moonphase == 26:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。有明月は夜明けごろに出てくるよ。"
elif moonphase == 27:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。"
elif moonphase == 28:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。"
elif moonphase == 29:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。"
elif moonphase == 30:
  tweet = "きょうの月齢は " + str(moonphase) + " だよ。三十日月。もうすぐ新月だね。"
else:
  tweet = "うーん。計算できなかったみたい。"

params = { 'status': tweet }
result = client.make_request(url,
                             token = user_token,
                             secret = user_secret,
                             additional_params = params,
                             method = 'POST')

print 'Content-Type: text/plain'
print ''
print result.content