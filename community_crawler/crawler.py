from selenium import webdriver

class Crawler:
    def __init__(self, url):
        self.driver = webdriver.Chrome('chromedriver_90.exe')
        self.driver.implicitly_wait(3)
        self.driver.get(url)