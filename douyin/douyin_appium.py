# -*- coding: utf-8 -*-

import time
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['appPackage'] = 'com.ss.android.ugc.aweme'
desired_caps['appActivity'] = 'com.ss.android.ugc.aweme.splash.SplashActivity'
desired_caps['noReset'] = True
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://192.168.1.100:4723/wd/hub', desired_caps)

def get_size(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x,y)

def handle_douyin(driver):
    #处理权限
    try:
        while WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath("//android.widget.TextView[@resource-id='android:id/le_bottomsheet_default_title']")):
            driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.android.packageinstaller:id/permission_allow_button']").click()
    except:
        pass

    try:
        #点击搜索
        if WebDriverWait(driver,30).until(lambda x:x.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.ss.android.ugc.aweme:id/ab_']")):
            driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.ss.android.ugc.aweme:id/ab_']").click()
    except:
        #通过坐标定位搜索控件
        driver.tap([(478, 23), (522, 50)], 500)

    for x in range(1,5):
        try:
            #定位搜索框
            if WebDriverWait(driver,3).until(lambda x:x.find_element_by_xpath("//android.widget.EditText[@resource-id='com.ss.android.ugc.aweme:id/a8g']")):
                #获取douyin_id进行搜索
                driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.ss.android.ugc.aweme:id/a8g']").set_value('lwnx1208')
                while driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.ss.android.ugc.aweme:id/a8g']").text != 'lwnx1208':
                    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.ss.android.ugc.aweme:id/a8g']").clear()
                    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.ss.android.ugc.aweme:id/a8g']").set_value('lwnx1208')
                    time.sleep(0.1)
            break
        except:
            time.sleep(0.5)


    #点击搜索
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.ss.android.ugc.aweme:id/d7r']").click()
    #点击用户标签
    if WebDriverWait(driver,3).until(lambda x:x.find_element_by_xpath("//android.widget.TextView[@text='用户']")):
        driver.find_element_by_xpath("//android.widget.TextView[@text='用户']").click()
    time.sleep(2)
    try:
        #点击头像
        if WebDriverWait(driver,3).until(lambda x:x.find_element_by_xpath("//android.support.v7.widget.RecyclerView[@resource-id='com.ss.android.ugc.aweme:id/kh']/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]")):
            driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[@resource-id='com.ss.android.ugc.aweme:id/kh']/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
    except:
        pass

    try:
        #点击粉丝按钮
        if WebDriverWait(driver,3).until(lambda x:x.find_element_by_xpath("//android.widget.TextView[@resource-id='com.ss.android.ugc.aweme:id/a6a']")):
            driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.ss.android.ugc.aweme:id/a6a']").click()
    except:
        pass

    l = get_size(driver)
    x1 = int(l[0]*0.5)
    y1 = int(l[1]*0.75)
    y2 = int(l[1]*0.25)
    while True:
        if '没有更多了' in driver.page_source:
            break
        driver.swipe(x1,y1,x1,y2)
        time.sleep(0.5)


if __name__ == '__main__':
    handle_douyin(driver)
