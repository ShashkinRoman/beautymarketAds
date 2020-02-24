import os
from distutils.command.config import config
from time import sleep
from webdriver import webdriver_conf
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from data_parse import fb_authorization
from config import Weekday
load_dotenv()


# не считаются первые 6 диалогов
def first_scrolling(driver): #todo клик перенести в мейн, здесь оставить только скролл, разбить на первый скрол и последующие
    scroll = driver.find_element_by_xpath(
        '//*[@id="u_0_u"]/div/div/div/table/tbody/tr/td[2]/div/div/div[2]/div/div/div/div[2]/div/div[11]/div')
    scroll.click()


# 1 страница 9 диалогов и 18 скролов
def scrolling(driver):
    scroll = driver.find_element_by_xpath(
        '//*[@id="u_0_u"]/div/div/div/table/tbody/tr/td[2]/div/div/div[2]/div/div/div/div[2]/div/div[11]/div')
    for i in range(0, 19):
        scroll.send_keys(Keys.ARROW_DOWN)
        sleep(0.5)


# ищем все даты элементов на странице
def find_leads(driver):
    driver = driver
    leads = driver.find_elements_by_class_name('timestamp')
    return leads


# считаем количество всех лидов за указанную дату
def count_leads(counter=0):
    a = 0
    counter_funk = counter
    driver = webdriver_conf.Webdriver.driver
    weekday = Weekday()
    yesterday = weekday.text_day(weekday.yesterday_datetime)
    day_before_yesterday = weekday.text_day(weekday.day_before_yesterday_datetime)
    leads = find_leads(driver)
    for lead in leads:
        if lead.get_attribute('title') == yesterday:
            counter_funk += 1
        if lead.get_attribute('title') == day_before_yesterday:
            print(counter_funk)
            a = 1
    else:
        if a == 1:
            return counter + counter_funk
        scrolling(driver)
        count_leads(counter_funk)
    # if counter_funk > 0:
    #     scrolling(driver)
    #     count_leads(driver, yesterday, day_before_yesterday, counter)
    # scrolling(driver)
    # count_leads(driver, yesterday, day_before_yesterday, counter)

def main():
    driver = webdriver_conf.Webdriver.driver
    fb_authorization(driver)
    driver.get(os.getenv('url_bm_messages'))
    # weekday = Weekday()
    # yesterday = weekday.text_day(weekday.yesterday_datetime)
    # day_before_yesterday = weekday.text_day(weekday.day_before_yesterday_datetime)
    sleep(2)
    first_scrolling(driver)
    lead = count_leads(counter=0)
    return lead


if __name__ == '__main__':
    main()
