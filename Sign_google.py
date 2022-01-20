import random
import time
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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


def input_dependence():
    global driver, shadow
    # 启动浏览器内核
    opt = ChromeOptions()
    opt.headless = False
    # path_e = os.getcwd() + r"\buster.crx"
    # opt.add_extension(path_e)
    # path_e = os.getcwd() + r"\AutoVerify.crx"
    # opt.add_extension(path_e)
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
    # shadow = Shadow(driver)
    driver.set_page_load_timeout(300)






def main():
    input_dependence()
    driver.get('https://www.spiritlhl.top/')
    time.sleep(3)
    driver.get('https://www.spiritlhl.top/')
    time.sleep(60)
    WebDriverWait(driver, 30, 1).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/main/div/div/div/div[2]')))
    driver.switch_to.frame(driver.find_element(By.NAME, 'aswift_1'))
    eles = driver.find_elements(By.TAG_NAME, 'a')
    list_urls = []
    for i in eles:
        if 'double' in i.get_attribute('href'):
            list_urls.append(i.get_attribute('href'))
    list_urls = list(set(list_urls))
    for j in list_urls:
        driver.get(j)
        print(translator.trans("点击了:"))
        print(j)
        time.sleep(random.uniform(10, 30))

def close_driver():
    global driver, contents
    # 关闭浏览器内核
    try:
        driver.quit()
    except Exception as e:
        print(e)
        print("driver closed")
    print(translator.trans("关闭浏览器内核完毕"))
    contents.append(translator.trans("关闭浏览器内核完毕"))


translator = LanguageTrans("C2E")
if __name__ == '__main__':
    print("=================================================")
    print(translator.trans("开始脚本运行"))
    try:
        print(1)
        main()
        close_driver()
    except:
        try:
            print(2)
            main()
            close_driver()
        except:
            pass
    print(translator.trans("结束脚本运行"))
