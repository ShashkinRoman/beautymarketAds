import os
from time import sleep
from datetime import datetime, timedelta
from webdriver import webdriver_conf
from dotenv import load_dotenv
load_dotenv()


# авторизируемся в фейсбуке
def fb_authorization(driver):
    f_driver = driver
    f_driver.get("https://www.facebook.com/ads/manager/accounts/")
    # find_id = webdriver_conf.w_id()
    # search and input login
    login = f_driver.find_element_by_id('email')
    # login.click()
    login.send_keys(os.getenv('log'))
    # search and input pass
    password = f_driver.find_element_by_id('pass')
    password.send_keys(os.getenv('pass'))
    # search and click button login
    login_button = f_driver.find_element_by_id('loginbutton')
    login_button.click()
    return f_driver

# импортируется здесь, чтобы не было ошибки импорта при выполнении leads_from_instagram
from leads_from_inst import main as main_leads_from_inst


# авторизируемся в моем складе
def ms_authorization(driver):
    f_driver = driver
    f_driver.get("https://www.moysklad.ru/")
    try:
        log_button = f_driver.find_element_by_xpath('/html/body/div[3]/header/div/a[3]')
        log_button.click()
        sleep(3)
    except:
        log_button = f_driver.find_element_by_xpath('/html/body/div[3]/header/div/div/nav/ul/li[6]/a')
        log_button.click()
        sleep(3)
    try:
        # Проверено с новой страничкой
        sleep(3)
        login = f_driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div[1]/form/fieldset[1]/input')
        # login.click()
        login.send_keys(os.getenv('mslog'))
        # search and input pass
        password = f_driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div[1]/form/fieldset[2]/input')
        password.send_keys(os.getenv('mspass'))
        # search and click button login
        login_button = f_driver.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div/div[2]/div[1]/form/fieldset[3]/button')
        login_button.click()
    except:
        # проверено со старой страницей
        login = f_driver.find_element_by_xpath('/html/body/div[3]/main/div[1]/div/div[2]/div[1]/form/fieldset[1]/input')
        # login.click()
        login.send_keys(os.getenv('mslog'))
        # search and input pass
        password = f_driver.find_element_by_xpath(
            '/html/body/div[3]/main/div[1]/div/div[2]/div[1]/form/fieldset[2]/input')
        password.send_keys(os.getenv('mspass'))
        # search and click button login
        login_button = f_driver.find_element_by_xpath(
            '/html/body/div[3]/main/div[1]/div/div[2]/div[1]/form/fieldset[3]/button')
        login_button.click()

    return f_driver


# получаем корректные дату для вставки в урлы
def yesterday_url():
    today = datetime.now()
    yesterday = today + timedelta(days=-1)
    if yesterday.day < 10:
        day = '0' + str(yesterday.day)
    else:
        day = str(yesterday.day)
    if yesterday.month < 10:
        month = '0' + str(yesterday.month)
    else:
        month = str(yesterday.month)
    if yesterday.day < 10:
        day_now = '0' + str(today.day)
    else:
        day_now = str(today.day)
    if yesterday.month < 10:
        month_now = '0' + str(today.month)
    else:
        month_now = str(today.month)
    yesterday_for_url = day + '-' + month + '-' + str(yesterday.year) + '_' + day_now + '-' + month_now + '-' + str(today.year)
    # print('yesterday_for_url', yesterday_for_url)
    yesterday_for_url_ms = day + '.' + month + '.' + str(yesterday.year) + '%2000:00:00,' + day + '.' + month_now + '.' + str(today.year) + '%2023:59:59'
    url = os.getenv('url_first_part') + yesterday_for_url +os.getenv('url_second_part')
    urlms = os.getenv('msurl_yesterday_one_part') + str(yesterday_for_url_ms) + os.getenv('msurl_yesterday_two_part')
    # print('url', url)
    # print('urlms', urlms)
    return str(url), str(urlms)


# получаем данные по затратам на рекламу за вчерашний день
def get_info_fb(fb_driver, url):
    driver = fb_driver
    driver.get(url)
    sum = driver.find_elements_by_class_name('_1876')
    # print(sum[1].text)
    summa = sum[1].text[0:-2]
    final_sum = summa.replace(' ', '')
    # print(final_sum)
    return final_sum


# получаем информацию из моего склада
def get_info_ms(driver, url_ms):
    ms_driver = driver
    ms_driver.get(url_ms)
    sleep(3)
    ms_driver.execute_script("window.scrollBy(0,3000)")
    val = ms_driver.find_element_by_xpath('//*[@id="DocumentTablePnl"]/tfoot/tr[2]/th[6]/div')
    final_val = str(val.text).replace(' ', '')
    # print(final_val)
    cost = ms_driver.find_element_by_xpath(
        '/html/body/div[4]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr/td/div/div/table/tbody/tr[5]/td/table/tfoot/tr[2]/th[8]/div')
    final_cost = str(cost.text).replace(' ', '')
    # print(final_cost)
    ms_driver.execute_script("window.scrollBy(0,-3000)")
    button_buyer = ms_driver.find_element_by_xpath(
        '//*[@id="site"]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr/td/div/div/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr/td[2]/table/tbody/tr/td[1]/div/div[3]')
    button_buyer.click()
    sleep(3)
    ms_driver.execute_script("window.scrollBy(0,3000)")
    documents = ms_driver.find_element_by_class_name('pages')
    final_doc = str(documents.text).split()[-1]
    # print(final_doc)
    return final_val, final_cost, final_doc


def main():
    url_fb, url_ms = yesterday_url()
    driver = webdriver_conf.Webdriver.driver
    fb_driver = fb_authorization(driver)
    fb_result = get_info_fb(fb_driver, url_fb)
    fb_leads = main_leads_from_inst()
    ms_driver = ms_authorization(driver)
    final_val, final_cost, final_doc = get_info_ms(ms_driver, url_ms)

    driver.close()
    return final_val, final_cost, final_doc, fb_result , fb_leads


if __name__ == '__main__':
    main()
