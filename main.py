# -*- coding: utf-8 -*-  
import mail
import simplejson
import urllib2
import time
from config import *

def moniter(m, send_to, high, low):

    if currency == 'CHN':
        url = 'http://data.btcchina.com/data/ticker'
    else:
        url = 'https://blockchain.info/ticker'

    req = urllib2.Request(url)
    opener = urllib2.build_opener()
    last_sent = 0

    while True:
        try:
            f = opener.open(req)
            data = simplejson.load(f)
        except:
            time.sleep(3)
            continue

        if currency == 'CHN':
            price = float(data['ticker']['last'])
            buy = data['ticker']['buy']
            sell = data['ticker']['sell']
            symbol = '￥'
        else:
            price = float(data[currency]['last'])
            buy = str(data[currency]['buy'])
            sell = str(data[currency]['sell'])
            symbol = str(data[currency]['symbol'])

        if price > high or price < low:
            if time.time() - last_sent > 5 * 60:
                try:
                    m.send(send_to, "BTC Ticker Warning", 
                           "the price now is " + str(price))
                    print "sent email"
                    last_sent = time.time()
                except Exception, e:
                    print e

        print("Price: " + symbol + str(price) + " Buy: " + symbol + buy + "  Sell: " + symbol + sell)
        time.sleep(3)

if __name__ == "__main__":
    m = mail.Mail(account, smtp_addr, account, password)
    moniter(m, send_to, high, low)
