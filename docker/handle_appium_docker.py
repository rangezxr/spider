# -*- coding: utf-8 -*-

import time
import multiprocessing
from appium import webdriver
import random

def get_size(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x,y)

def handle_appium(info):
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '5.1.1',
        'deviceName': info['device'],
        'udid': info['device'],
        'appPackage':  info['appPackage'],
        'appActivity':  info['appActivity'],
        'noReset': True,
        'unicodeKeyboard': True,
        'resetKeyboard': True,
    }
    driver = webdriver.Remote(host, desired_caps)

    l = get_size(driver)
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.75)
    y2 = int(l[1] * 0.25)

    appPackage_list = ['com.ss.android.ugc.aweme', 'com.simle.gifmaker', 'com.simle.gifmaker']

    if info['appPackage'] in appPackage_list:
        while True:
            try:
                # 初始鼠标的位置，从哪开始，结束是鼠标位置，到哪结束
                driver.swipe(x1, y1, x1, y2)
                time_list = [5, 10, 8, 3, 11]
                time.sleep(random.choice(time_list))
            except:
                print('滑动失败')

if __name__ == "__main__":
    m_list = []
    #定义虚拟设备
    devices_list = [
        {
            "device": "192.168.199.132:5555",
            "appPackage": "com.ss.android.ugc.aweme",
            "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
            "port": "4723",
            "key": "抖音",
        },
        {
            "device": "192.168.199.133:5555",
            "appPackage": "com.simle.gifmaker",
            "appActivity": "com.yxcorp.gifshow.HomeActivity",
            "port": "4725",
            "key": "快手",
        },
        {
            "device": "192.168.199.134:5555",
            "appPackage": "com.ss.android.article.news",
            "appActivity": "com.ss.android.article.news.activiy.SplashBadgeActivity",
            "port": "4725",
            "key": "今日头条",
        }
    ]

    for device in (devices_list):
        m_list.append(multiprocessing.Process(target=handle_appium,args=(device,)))

    for m1 in m_list:
        m1.start()
