#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 19:45:44 2017

@author: Frances
"""

import tweepy, time, sys
 
argfile = str(sys.argv[1])
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'niSQqQ520rgz3RiZhXeNHpGUU'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'bwZbScef4KRqLvbvtYx5TQCPluR7Ck18HT9lckWhiM3eskC6Hf'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '915762294562234368-Pez4mZap3REoLalfHsEM89tSQBAUU1Z'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'dksum1yOOX7xQf9yG64nil8Bw5HhceiJsSb6y7kBupxDZ'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
filename=open(argfile,'r')
f=filename.readlines()
filename.close()
 
for line in f:
    print(line)
    api.update_status(line)
    time.sleep(900)#Tweet every 15 minutes