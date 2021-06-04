#!/usr/bin/env python
# coding: utf-8

import time
import configparser
from datetime import datetime
from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from news import newslist
from kaia import kaialist
from job import joblist




def news():
    browser.get(news_url)        # URL 변경

    for i in range(len(newslist)):
        # 글 등록
        enroll = browser.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/div[2]/div[1]/div[4]/button")
        enroll.click()

        # 제목
        title = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div[2]/div[2]/div[2]/div[1]/div/form/fieldset/div/div[1]/div/div[2]/input")))
        title.send_keys(newslist[i]['title'])


        # 콤보박스
        time.sleep(1)
        select = Select(browser.find_element_by_id("system"))
        select.select_by_index(1)

        # 글 내용
        time.sleep(1)
        content = browser.find_element_by_tag_name("iframe")
        browser.switch_to.frame(content)
        content_write = browser.find_element_by_xpath("/html/body/p")
        # content_write = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/p")))
        content_write.click()
        content_write.send_keys(newslist[i]['pdate'] + "\n\n")
        content_write.send_keys(newslist[i]['description'] + "\n\n\n\n")
        content_write.send_keys(Keys.CONTROL,"k")
        browser.switch_to.default_content()

        
        # 링크 및 보이는 글자 삽입
        time.sleep(1)
        url_input = newslist[i]['link']
        actions = ActionChains(browser)
        actions.send_keys(url_input)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.TAB)
        
        time.sleep(3)
        actions.send_keys(" 링크 : " + url_input)
        actions.perform()
        
        
        # 타겟 새 창으로 설정
        target = browser.find_element_by_xpath("// a [contains (text (), '타겟')]")
        target.click()
            
        select_target = Select(browser.find_element_by_xpath("/html/body/div[3]/table/tbody/tr/td/div/table/tbody/tr[1]/td/div[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/div/div/div/select"))
        select_target.select_by_index(3)
        confirm = browser.find_element_by_xpath("/html/body/div[3]/table/tbody/tr/td/div/table/tbody/tr[2]/td/table/tbody/tr/td[1]")
        confirm.click()


        # 확인 버튼
        time.sleep(1)
        browser.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/div[2]/div[2]/button[2]").click()
        
        
        # 팝업 닫기
        time.sleep(1)
        popup = Alert(browser)
        popup.accept()
        
        # 연속 등록 막힘
        time.sleep(15)

def kaia():
    browser.get(kaia_url)        # URL 변경

    for i in range(len(kaialist)):
        enroll = browser.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/div[2]/div[1]/div[6]/button/span")
        enroll.click()

        title = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div[2]/div[2]/div[2]/div[1]/div/form/fieldset/div/div[1]/div/div[2]/input")))
        title.send_keys(kaialist[i]['title'])

        time.sleep(1)

        content = browser.find_element_by_tag_name("iframe")
        browser.switch_to.frame(content)
        content_write = browser.find_element_by_xpath("/html/body/p")
        content_write.click()
        content_write.send_keys(kaialist[i]['description'] + "\n\n\n\n")
        content_write.send_keys(Keys.CONTROL,"k")
        browser.switch_to.default_content()

        time.sleep(1)

        url_input = kaialist[i]['link']
        actions = ActionChains(browser)
        actions.send_keys(url_input)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.TAB)
        
        time.sleep(3)

        actions.send_keys(" 링크 : " + url_input)
        actions.perform()
        
        target = browser.find_element_by_xpath("// a [contains (text (), '타겟')]")
        target.click()
            
        select_target = Select(browser.find_element_by_xpath("/html/body/div[3]/table/tbody/tr/td/div/table/tbody/tr[1]/td/div[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/div/div/div/select"))
        select_target.select_by_index(3)
        confirm = browser.find_element_by_xpath("/html/body/div[3]/table/tbody/tr/td/div/table/tbody/tr[2]/td/table/tbody/tr/td[1]")
        confirm.click()

        time.sleep(1)

        browser.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/div[2]/div[2]/button[2]").click()

        time.sleep(1)

        popup = Alert(browser)
        popup.accept()

        time.sleep(15)

def job():
    browser.get(job_url)

    for i in range(len(joblist)):
        enroll = browser.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/div[2]/div[1]/div[3]/button")
        enroll.click()

        title = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div[2]/div[2]/div[2]/div[1]/div/form/fieldset/div/div[1]/div/div[2]/input")))
        title.send_keys(joblist[i]['title'])

        time.sleep(1)

        select = Select(browser.find_element_by_id("system"))
        select.select_by_index(3)

        time.sleep(1)

        content = browser.find_element_by_tag_name("iframe")
        browser.switch_to.frame(content)
        content_write = browser.find_element_by_xpath("/html/body/p")
        content_write.click()
        content_write.send_keys(joblist[i]['description'] + "\n\n\n\n")
        content_write.send_keys(Keys.CONTROL,"k")
        browser.switch_to.default_content()

        time.sleep(1)

        url_input = joblist[i]['link']
        actions = ActionChains(browser)
        actions.send_keys(url_input)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.TAB)
        
        time.sleep(3)

        actions.send_keys(" 링크 : " + url_input)
        actions.perform()
        
        target = browser.find_element_by_xpath("// a [contains (text (), '타겟')]")
        target.click()
            
        select_target = Select(browser.find_element_by_xpath("/html/body/div[3]/table/tbody/tr/td/div/table/tbody/tr[1]/td/div[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/div/div/div/select"))
        select_target.select_by_index(3)
        confirm = browser.find_element_by_xpath("/html/body/div[3]/table/tbody/tr/td/div/table/tbody/tr[2]/td/table/tbody/tr/td[1]")
        confirm.click()

        time.sleep(1)

        browser.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/div[2]/div[2]/button[2]").click()
        
        time.sleep(1)

        popup = Alert(browser)
        popup.accept()
        
        time.sleep(15)



if __name__ == '__main__':
    
    
    conf = configparser.ConfigParser()
    conf.read("./conf/config.ini")

    section = "URL"
    news_url = conf.get(section, 'news')
    kaia_url = conf.get(section, 'kaia_matching')
    job_url = conf.get(section, 'job_info')
    


    section = "ACCOUNT"
    user = conf.get(section, 'user')
    password = conf.get(section, 'password')

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome(options=options)
    browser.get("https://data.molit.go.kr/member/login")
    wait = WebDriverWait(browser, 10)

    user_id = browser.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/div[2]/div/form/fieldset/div/div[1]/input").send_keys(user)
    password = browser.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div[2]/div/form/fieldset/div/div[2]/input').send_keys(password, Keys.ENTER)


    time.sleep(2)

    news()
    kaia()
    # job()
    
    browser.quit()