# 作者仓库:https://github.com/spiritLHL/Gecko_sign
# 觉得不错麻烦点个star谢谢

users = ["xxxxxxxxx", "xxxxxxxxxxx"]
passwords = ["xxxxxx", "xxxxxxxx"]




users = ["13692603682"]
passwords = ["246@100l6717hl"]


import random
import time
import os
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pyshadow.main import Shadow



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
    ser = Service("chromedriver.exe")
    driver = Chrome(service=ser, options=opt)
    # 加载影子模块
    shadow = Shadow(driver)
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
        print("选项显示的文本：", option.text)
        print("选项值为：", option.get_attribute("value"))
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
    print("加载用户 {}".format(user))
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
        print("签到页面加载失败，正在刷新页面。。。")
        print("第{}次重新登陆".format(count + 1))
        load_sign(user, password)
        driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_btnCreate"]').click()
        time.sleep(random.uniform(10, 30))
        count += 1
        if count >= 10:
            print("签到页面加载失败，建议过大半天再次运行脚本避免黑号\n")
            exit(3)
    print("签到页面加载完毕，正在签到。。。")
    # 签到操作
    load_driver("https://www.sojiang.com/newsojiang/mobile/userdetail.aspx")
    time.sleep(random.uniform(5, 7))
    driver.find_element(By.XPATH, '//*[@id="form1"]/header/div[2]/a[1]').click()
    print("已点击签到，正在等待签到结果。。。")
    time.sleep(5)
    try:
        result = driver.find_element(By.XPATH, '//*[@id="layui-layer1"]/div[2]').text
        print("执行结果： {}".format(result))
    except:
        print("已签到")
    # 关闭浏览器内核
    driver.close()
    try:
        driver.quit()
    except:
        print("driver 已经关闭")
    print("关闭浏览器内核完毕")
    print("====================================")


if __name__ == '__main__':
    print("开始脚本运行")
    for i, j in zip(users, passwords):
        main(i, j)
        time.sleep(random.uniform(10, 30))
    print("结束脚本运行")
