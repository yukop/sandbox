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
params = { 'status': "きょうの月齢は " + str(moonphase) + " だよー！"}
result = client.make_request(url,
                             token = user_token,
                             secret = user_secret,
                             additional_params = params,
                             method = 'POST')

print 'Content-Type: text/plain'
print ''
print result.content