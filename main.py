# -*- coding: utf-8 -*-
import mail
import simplejson
import urllib2
import time
from config import *


def moniter(m, send_to, high, low):

    req = urllib2.Request("https://data.btcchina.com/data/ticker")
    opener = urllib2.build_opener()
    last_sent = 0

    while True:
        try:
            f = opener.open(req)
            data = simplejson.load(f)
        except:
            time.sleep(3)
            continue

        price = float(data['ticker']['last'])
        if price > high or price < low:
            for i in range(3):
                try:
                    if time.time() - last_sent > 5 * 60:
                        m.send(send_to, "BTC Ticker Warning",
                            "the price now is " + str(price))
                except:
                    continue
                last_sent = time.time()
                break

        print "Price: ￥%s  Buy: ￥%s  Sell: ￥%s" % (data['ticker']['last'],
                    data['ticker']['buy'], data['ticker']['sell'])
        time.sleep(3)


if __name__ == "__main__":
    m = mail.Mail(account, smtp_addr, account, password)
    moniter(m, send_to, high, low)
