from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import pyautogui as pg
import pyperclip as pc

#set initial infomation:
os.chdir('firefox_tool_path')
url = oa_url

#import the data that should input to sheet of workflows.
info = pd.read_csv('data.csv',encoding='GBK')

#set a list to filter the data.
l = list(range(25))
l.reverse()

#locate somes point positions in order to using pyautogui to control mouse.
s = (1069,820)
xjlc = (129,472)
ljzrs = (450,431)
bt = (602,297)
qybm = (529,537)
title = (584,629)
xingming = (580,674)
shouji = (1557,674)

u = '2020年廉洁责任书'

    
def inter(point,content):
    '''using pyguiauto and pyperclip to input info to brower when we cant locate the essintial elements'''
    pg.click(point)
    time.sleep(0.5)
    pc.copy(content)
    pg.hotkey('ctrl','v')
    time.sleep(0.5)

def itera(initial_position,name_list,n):
    '''for the structure of sheet,we defined a function to fill the sheet orderly'''
    pg.moveTo(initial_position)
    for y in range(4):
        pg.click()
        inter(pg.position(),str(info.iloc[n][name_list[y]]))
        time.sleep(1)
        pg.moveRel((0,143))
    

def txbd(n):
    '''assemble the intera() function'''
    time.sleep(1)
    inter(bt,info.iloc[n]['name']+u)
    inter(qybm,info.iloc[n]['name'])
    itera(title,['at','bt','ct','dt'],n)
    itera(xingming,['a','b','c','d'],n)
    itera(shouji,['am','bm','cm','dm'],n)
    
for i in l:
    browser = webdriver.Firefox()
    browser.get(url)
    browser.maximize_window()
    time.sleep(1)
    elem = browser.find_element_by_name('loginid')
    elem.send_keys('username')
    elem = browser.find_element_by_name('userpassword')
    elem.send_keys('password' + Keys.RETURN)
    time.sleep(5)
    pg.click(s)
    pg.click(s)
    time.sleep(1)
    browser.find_elements_by_id('null')[0].click()
    time.sleep(3)
    for p in range(3):
        pg.click(xjlc)
        time.sleep(0.5)
    time.sleep(2)
    pg.click(ljzrs)
    time.sleep(5)
    windows = browser.window_handles
    browser.switch_to.window(windows[-1])
    browser.maximize_window()
    
    txbd(i)
    browser.save_screenshot(f'D:\\{i}.png')
    time.sleep(2)
    pg.click((1997,149))
    time.sleep(5)
    browser.quit()