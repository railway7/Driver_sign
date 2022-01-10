# 作者仓库:https://github.com/spiritLHL/Gecko_sign
# 觉得不错麻烦点个star谢谢
# 注册页面 http://www.sojiang.com/i.aspx?c=1-11501664
# 只适配Windows，不适配Linux，Linux环境下无法加载插件

# local
users = ["xxxxxxxxx", "xxxxxxxxxxx"]
passwords = ["xxxxxx", "xxxxxxxx"]

# AC
import sys

if len(sys.argv) < 2:
    print('argv Error')
else:
    users = [sys.argv[1]]
    passwords = [sys.argv[2]]
    if " " in users[0] and " " in passwords[0]:
        users = users[0].split(" ")
        passwords = passwords[0].split(" ")

print(users, passwords)


import random
import time
import os
import re
import zipfile
import requests
import pyshadow
import selenium
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from translate import Translator

class LanguageTrans():
    def __init__(self, mode):
        self.mode = mode
        if self.mode == "E2C":
            self.translator = Translator(from_lang="english", to_lang="chinese")
        if self.mode == "C2E":
            self.translator = Translator(from_lang="chinese", to_lang="english")
    def trans(self, word):
        translation = self.translator.translate(word)
        return translation




def get_latest_version(url):
    '''查询最新的Chromedriver版本'''
    rep = requests.get(url).text
    time_list = []                                          # 用来存放版本时间
    time_version_dict = {}                                  # 用来存放版本与时间对应关系
    result = re.compile(r'\d.*?/</a>.*?Z').findall(rep)     # 匹配文件夹（版本号）和时间
    for i in result:
        time = i[-24:-1]                                    # 提取时间
        version = re.compile(r'.*?/').findall(i)[0]         # 提取版本号
        time_version_dict[time] = version                   # 构建时间和版本号的对应关系，形成字典
        time_list.append(time)                              # 形成时间列表
    latest_version = time_version_dict[max(time_list)][:-1] # 用最大（新）时间去字典中获取最新的版本号
    return latest_version

def download_driver(download_url):
    '''下载文件'''
    file = requests.get(download_url)
    with open(r"chromedriver.zip", 'wb') as zip_file:        # 保存文件到脚本所在目录
        zip_file.write(file.content)
        print(translator.trans('下载成功'))

def get_version():
    '''查询系统内的Chromedriver版本'''
    outstd2 = os.popen('chromedriver --version').read()
    return outstd2.split(' ')[1]

def get_path():
    '''查询系统内Chromedriver的存放路径'''
    outstd1 = os.popen('where chromedriver').read()
    return outstd1.strip('chromedriver.exe')

def unzip_driver(path):
    '''解压Chromedriver压缩包到指定目录'''
    f = zipfile.ZipFile(r"chromedriver.zip", 'r')
    for file in f.namelist():
        f.extract(file, path)

# def un_zip(csv_path):
# 	for f in  os.listdir(csv_path):
# 		if ".zip" in f:
# 			zip_file = zipfile.ZipFile(csv_path + "\\" + f)
# 			zip_file.extract(zip_file.namelist()[0],csv_path)



def input_dependence():
    global driver, shadow
    # 启动浏览器内核
    opt = ChromeOptions()
    opt.headless = False
    # path_e = os.getcwd() + r"\buster.crx"
    # opt.add_extension(path_e)
    path_e = os.getcwd() + r"\AutoVerify.crx"
    opt.add_extension(path_e)
    opt.add_argument("window-size=1920,1080")
    # opt.add_experimental_option('prefs', prefs)  # 关掉浏览器左上角的通知提示
    # opt.add_argument("disable-infobars")  # 关闭'chrome正受到自动测试软件的控制'提示
    opt.add_argument('--no-sandbox')
    # 设置开发者模式启动，该模式下webdriver属性为正常值
    opt.add_experimental_option('excludeSwitches', ['enable-automation'])
    # opt.add_argument({"extensions.ui.developer_mode": True})
    # opt.add_experimental_option('useAutomationExtension', False)
    # opt.set_preference("extensions.firebug.allPagesActivation", "on")
    opt.add_experimental_option('excludeSwitches', ['enable-logging'])
    ser = Service("chromedriver")
    driver = Chrome(service=ser, options=opt)
    # 加载影子模块
    shadow = pyshadow.main.Shadow(driver)
    driver.set_page_load_timeout(300)

def change_seeting():
    global driver, shadow
    element = shadow.find_element("#devMode")
    element.click()
    time.sleep(3)
    element = shadow.find_element('#detailsButton')
    time.sleep(2)
    element.click()
    time.sleep(2)
    element = shadow.find_element('#host-access')
    element.click()
    # element.click()
    # element.send_keys(Keys.CONTROL + Keys.DOWN + Keys.DOWN + Keys.ENTER)
    all_options = element.find_elements(By.TAG_NAME, "option")
    for option in all_options:
        try:
            print(translator.trans("选项显示的文本 "), translator.trans(option.text))
            print(translator.trans("选项值为 "), translator.trans(option.get_attribute("value")))
        except:
            print(translator.trans("选项显示的文本 "), option.text)
            print(translator.trans("选项值为 "), option.get_attribute("value"))
    # WebDriverWait(option, 3, 0.1).until(EC.element_to_be_clickable((By.LINK_TEXT, '在所有网站上'))).click()
    time.sleep(2)
    option.click()
    element = shadow.find_element('#centeredContent')
    time.sleep(2)
    element.click()
    time.sleep(2)
    element = shadow.find_element('#closeButton')
    time.sleep(2)
    element.click()
    time.sleep(2)


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


# def expand_shadow_element(element):
#     shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
#     driver.implicitly_wait(0.5)
#
#     return shadow_root



def load_sign(user, password):
    global driver
    load_driver("https://www.sojiang.com/newsojiang/login.aspx")
    time.sleep(random.uniform(1, 3))
    driver.find_element(By.XPATH,
                        '//*[@id="ctl00_ContentPlaceHolder1_regAntiSpam_txtValInputCode"]').click()
    time.sleep(random.uniform(3, 5))
    driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_UserName"]').send_keys(user)
    time.sleep(random.uniform(3, 5))
    driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_Password"]').send_keys(password)
    time.sleep(random.uniform(3, 5))


def main(user, password):
    print("====================================")
    print(translator.trans("加载用户 ").format(user))
    input_dependence()
    time.sleep(3)
    # 选项修改
    load_driver("chrome://extensions/")
    change_seeting()
    # change_seeting()
    time.sleep(10)
    # 登陆操作
    load_sign(user, password)
    driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_btnCreate"]').click()
    time.sleep(10)
    count = 0
    while driver.current_url == "https://www.sojiang.com/newsojiang/login.aspx":
        print(translator.trans("签到页面加载失败，正在刷新页面"))
        print("Number {} refresh pages".format(count + 1))
        load_sign(user, password)
        driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_btnCreate"]').click()
        time.sleep(random.uniform(10, 30))
        count += 1
        if count >= 10:
            print(translator.trans("签到页面加载失败，建议过大半天再次运行脚本避免黑号"))
            exit(3)
    print(translator.trans("签到页面加载完毕，正在签到"))
    # 签到操作
    load_driver("https://www.sojiang.com/newsojiang/mobile/userdetail.aspx")
    time.sleep(random.uniform(5, 7))
    driver.find_element(By.XPATH, '//*[@id="form1"]/header/div[2]/a[1]').click()
    print(translator.trans("已点击签到，正在等待签到结果"))
    time.sleep(5)
    try:
        result = driver.find_element(By.XPATH, '//*[@id="layui-layer1"]/div[2]').text
        print("result {}".format(result))
    except:
        print(translator.trans("已签到"))
    # 关闭浏览器内核
    driver.close()
    try:
        driver.quit()
    except:
        print("driver closed")
    print(translator.trans("关闭浏览器内核完毕"))
    print("====================================")

translator = LanguageTrans("C2E")
if __name__ == '__main__':
#     try:
#         url = 'http://npm.taobao.org/mirrors/chromedriver/'
#         latest_version = get_latest_version(url)
#         print(translator.trans('最新的chromedriver版本为 '), latest_version)
#         version = get_version()
#         print(translator.trans('当前系统内的Chromedriver版本为 ', version))
#         if version == latest_version:
#             print(translator.trans('当前系统内的Chromedriver已经是最新的'))
#         else:
#             print(translator.trans('当前系统内的Chromedriver不是最新的，需要进行更新'))
#             download_url = url + latest_version + '/chromedriver_win32.zip'  # 拼接下载链接
#             download_driver(download_url)
#             path = get_path()
#             unzip_driver(path)
#             # un_zip(path)
#             print(translator.trans('更新后的Chromedriver版本为'), get_version())
#     except:
#         pass
#         # url = 'http://npm.taobao.org/mirrors/chromedriver/'
#         # latest_version = get_latest_version(url)
#         # download_url = url + latest_version + '/chromedriver_win32.zip'  # 拼接下载链接
#         # download_driver(download_url)
#         # path = get_path()
#         # print('替换路径为：', path)
#         # unzip_driver(path)
#         # # un_zip(path)
#         # print('更新后的Chromedriver版本为：', get_version())
    print("=================================================")
    print(translator.trans("开始脚本运行"))
    for i, j in zip(users, passwords):
        main(i, j)
        time.sleep(random.uniform(10, 30))
    print(translator.trans("结束脚本运行"))
