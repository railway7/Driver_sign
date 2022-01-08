# 作者仓库:https://github.com/spiritLHL/Gecko_sign
# 觉得不错麻烦点个star谢谢
'''
cron: 8 8 * * *
new Env('领取腾讯云签到积分');
'''


'''
cron: 8 8 * * *
new Env('领取腾讯云签到积分');
'''




users = ["xxxxxx@163.com", "xxxxxxxx@qq.com"]
passwords = ["xxxxxxxxxxxx", "xxxxxxx"]



import requests
import random
import re
import time
import json
from lxml import html
from bs4 import BeautifulSoup
from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from requests.adapters import HTTPAdapter


def input_dependence():
    global driver, s
    # 设置超时重试
    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=3))
    s.mount('https://', HTTPAdapter(max_retries=3))
    # 启动浏览器内核
    opt = FirefoxOptions()
    opt.headless = True
    ser = Service("geckodriver")
    driver = Firefox(service=ser, options=opt)
    driver.set_page_load_timeout(300)


def load_driver(url):
    global driver
    try:
        driver.get(url)
        return driver
    except TimeoutException:
        time.sleep(5)
        driver.delete_all_cookies()
        try:
            driver.get(url)
            return driver
        except TimeoutException:
            print('timeout')
            return


def main(user, password):
    print("====================================")
    print("加载用户 {}".format(user))
    input_dependence()
    print("加载浏览器内核完毕")
    load_driver("https://cloud.tencent.com/login?s_url=https%3A%2F%2Fcloud.tencent.com%2Fact%2Fintegralmall")
    wait = WebDriverWait(driver, 5, 0.1)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'clg-other-link')))
    time.sleep(random.uniform(3, 5))
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div/div/div[4]/div[2]/div[1]/a").click()
    print("跳转邮箱登陆中。。。。。")
    time.sleep(random.uniform(1, 3))
    driver.find_element(By.XPATH,
                        "/html/body/div[2]/div/div[1]/div[1]/div/div/div[2]/div[2]/ul/li[1]/div/div/input").send_keys(
        user)
    time.sleep(random.uniform(1, 3))
    driver.find_element(By.XPATH,
                        "/html/body/div[2]/div/div[1]/div[1]/div/div/div[2]/div[2]/ul/li[2]/div/div/input").send_keys(
        password)
    time.sleep(random.uniform(1, 3))
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/a[1]").click()
    time.sleep(random.uniform(5, 10))
    print("邮箱登陆完毕，等待签到页面加载。。。")
    try:
        result = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/div[1]/div/a").text
        if result == "已签到":
            print("用户 {} 已签到，自动跳过该账号".format(user))
            # 关闭浏览器内核
            driver.close()
            try:
                driver.quit()
            except:
                print("driver 已经关闭")
            print("关闭浏览器内核完毕")
            print("====================================")
            return
    except:
        pass
    try:
        wait = WebDriverWait(driver, 10, 0.2)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'bmh-oviewcard-cbtns-btn')))
        time.sleep(random.uniform(3, 5))
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/div[1]/div/a").click()
        print("签到页面加载完毕，正在签到。。。")
    except:
        try:
            print("签到页面加载失败，正在刷新页面。。。")
            load_driver("https://cloud.tencent.com/act/integralmall")
            wait = WebDriverWait(driver, 10, 0.2)
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'bmh-oviewcard-cbtns-btn')))
            time.sleep(random.uniform(3, 5))
            driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/div[1]/div/a").click()
            print("签到页面加载完毕，正在签到。。。")
        except:
            print("签到页面加载失败，建议先登陆账号关闭登陆保护再次执行，否则无法执行签到脚本\n")
            print("关闭教程：\n")
            print("关闭登录保护. 登录腾讯云控制台，进入 安全设置 页面，单击账号保护 > 登录保护右侧的编辑图标。. 根据页面提示，完成身份验证。. 通过身份验证后，勾选【不开启】后单击【确定】即可关闭登录保护。\n")
            print("具体图文教程：\n")
            print("https://cloud.tencent.com/document/product/378/8392\n")
            print("只需要关闭登陆保护，而不是关闭操作保护，操作保护别关闭。\n")
            print("如果关闭登陆保护后还是无法加载，请访问积分商城页面开通积分权益先。\n")
            print("积分商城链接：")
            # 关闭浏览器内核
            driver.close()
            try:
                driver.quit()
            except:
                print("driver 已经关闭")
            print("关闭浏览器内核完毕")
            print("====================================")
            return
    time.sleep(random.uniform(1, 3))
    wait = WebDriverWait(driver, 10, 0.2)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'dialog-box-content')))
    time.sleep(random.uniform(1, 3))
    driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[3]/button").click()
    print("已点击签到，正在等待签到结果。。。")
    time.sleep(random.uniform(5, 10))
    result = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[2]/div[2]/p").text
    print("用户{}签到结果为:\n {}".format(user, result))
    if " 积分稍后到账，连续签到将获得更多积分" in result:
        print("签到成功，待浏览器内核关闭。。。")
    # 关闭浏览器内核
    driver.close()
    try:
        driver.quit()
    except:
        print("driver 已经关闭")
    print("关闭浏览器内核完毕")
    print("====================================")
    return


if __name__ == '__main__':
    print("开始脚本运行")
    for i, j in zip(users, passwords):
        main(i, j)
        time.sleep(random.uniform(10, 30))
    print("结束脚本运行")
