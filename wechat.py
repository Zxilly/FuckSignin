import json
import os
import time
import urllib.parse
from datetime import datetime

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

auth_server_url = "https://authserver.jgsu.edu.cn/authserver/login?service=https%3A%2F%2Fehall.jgsu.edu.cn%2Flogin%3Fservice" \
                  "%3Dhttps%3A%2F%2Fehall.jgsu.edu.cn%2Fywtb-mobile%2Findex.html"

if __name__ == '__main__':
    if not os.getenv('CI'):
        raise Exception("Only available in CI")
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    if not username or not password:
        raise Exception("USERNAME or PASSWORD is not set")

    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone X'})
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(1)
    time.sleep(2)
    user_agent = driver.execute_script("return navigator.userAgent;")
    driver.get(auth_server_url)

    account_ele = driver.find_element(By.ID, 'username')
    account_ele.send_keys(username)
    password_ele = driver.find_element(By.ID, 'password')
    password_ele.send_keys(password)
    submit_ele = driver.find_element(By.ID, 'login_submit')
    submit_ele.click()

    time.sleep(2)

    driver.get('https://ehall.jgsu.edu.cn/appShow?appId=6414451678401763')

    time.sleep(2)

    cookies = driver.get_cookies()
    driver.quit()

    s = requests.Session()
    for cookie in cookies:
        s.cookies.set(cookie['name'], cookie['value'])
    s.headers = {
        'User-Agent': user_agent
    }

    save_url = "https://ehall.jgsu.edu.cn/xsfw/sys/swmlsfxyqtbjgsu/modules/xssq/savaStuMrqk.do"

    data = json.loads(os.getenv('WECHAT_DATA'))

    now = datetime.now()
    data['TXRQ'] = now.strftime('%Y-%m-%d')
    data['CZRQ'] = now.strftime('%b %d, %Y %H:%M:%S %p')

    resp = s.post(save_url,
                  data={
                      'data': json.dumps(data, ensure_ascii=False)
                  }, headers={"Referer": "https://ehall.jgsu.edu.cn/xsfw/sys/swmlsfxyqtbjgsu/*default/index.do"})
    print(resp.ok)
    print(resp.text)
