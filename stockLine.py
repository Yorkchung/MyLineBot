# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 14:37:37 2019

@author: 佑崧
"""

 # -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 10:14:10 2018

@author: 佑崧
"""

import twstock
import time
import requests

counterLine = 0
counterError = 0

print('程式開始執行！')
while True:

    real = twstock.realtime.get('2317')
    
    if real['success']:
        
        realprice = real['realtime']['latest_trade_price']
        if float(realprice) >= 50:
            print('鴻海目前股價：' + realprice)
            url_ifttt ='https://maker.ifttt.com/trigger/stockLINE/with/key/dmfSYkkQXD2WkuIv5gaeji?value1=' + realprice
            res1 = requests.get(url_ifttt)
            counterLine = counterLine + 1
        elif float(realprice) < 50:
            print('鴻海目前股價：' + realprice)
            url_ifttt ='https://maker.ifttt.com/trigger/2317stock/with/key/dmfSYkkQXD2WkuIv5gaeji?value1=' + realprice
            res1 = requests.get(url_ifttt)
            counterLine = counterLine + 1
        print('第' + str(counterLine) + '次發送LINE回傳訊息：' + res1.text)
        if counterLine >= 1:
            print('程式結束！')
            break
        
        for i in range(20):
            time.sleep(1)

    else:
            print('twstock 讀取錯誤，錯誤原因：' + real['rtmessage'])
            counterError = counterError + 1
            if counterError >= 3:  #最多錯誤3次
                print('程式結束！')
                break
            for i in range(10):
                time.sleep(1)


