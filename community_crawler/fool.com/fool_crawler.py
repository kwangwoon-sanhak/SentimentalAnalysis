import time
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from crawler import Crawler


url = "https://www.fool.com/quote/nyse/exxonmobil/xom/"
PAUSE_TIME = 2

class FOOL_CRAWLER(Crawler):
    def __init__(self, url):
        super().__init__(url)
        self.url = []

    def get_community_url(self):
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        #while True:
        for i in range(0, 100):
            self.driver.find_element_by_xpath('//*[@id="load-more"]').click()
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(PAUSE_TIME)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
            time.sleep(PAUSE_TIME)
            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        h4_element = self.driver.find_elements_by_tag_name('h4')

        for element in h4_element:
            # print(element)
            # print(element.find_element_by_tag_name('a').get_attribute('href'))
            self.url.append(element.find_element_by_tag_name('a').get_attribute('href'))

        print(len(self.url))


    def write_url_to_txt(self):
        with open("fool_community_url.txt", "w") as f:
            for url_element in self.url:
                f.write(url_element + "\n")

    def save_articles(self):
        with open("fool_community_url.txt", "r") as f:
            links = f.readlines()
            for link in links:
                self.read_article(link)

    def read_article(self, url):
        #crawling_words = ["investing", "earnings"]
        crawling_words = ["general", "dividends-income"]
        # if '/' in url:
        #     if url.split('/')[3] == crawling_words[0]:
        #         #https://www.fool.com/investing/2021/03/18/oil-prices-crash-by-8-on-geopolitical-tensions-rec/
        #         date_number = 4
        #     if url.split('/')[3] == crawling_words[1]:
        #         #https://www.fool.com/earnings/call-transcripts/2020/05/01/exxon-mobil-corp-xom-q1-2020-earnings-call-transcr.aspx
        #         date_number = 5
        #     if not (url.split('/')[3] in crawling_words):
        #         return

        if '/' in url:
            if url.split('/')[4] in crawling_words:
                #https://www.fool.com/investing/2021/03/18/oil-prices-crash-by-8-on-geopolitical-tensions-rec/
                date_number = 5
            if not (url.split('/')[4] in crawling_words):
                return

            try:
                file_name = "./articles/investing_{year}-{month}-{date}.txt".format(
                    year = url.split('/')[date_number],
                    month = url.split('/')[date_number + 1],
                    date = url.split('/')[date_number + 2])
            except:
                print("file_name error" + url)
                return

            self.driver.get(url)
            time.sleep(PAUSE_TIME)

            with open(file_name, 'a') as f:
                try:
                    article_content = self.driver.find_element_by_class_name('article-content')
                    article = article_content.find_elements_by_tag_name('p')
                    for paragraph in article:
                        f.write(paragraph.text + '\n')
                except:
                    print(file_name)

if __name__ == "__main__":
    PHASE = {1: "get_url", 2: "read_article"}
    current_phase = PHASE[2]

    if current_phase == "get_url":
        fool_crawler = FOOL_CRAWLER(url)
        fool_crawler.get_community_url()
        fool_crawler.write_url_to_txt()
    if current_phase == "read_article":
        fool_crawler = FOOL_CRAWLER(url)
        fool_crawler.save_articles()
             

#*[@id="page-1"]/article[1]/div[2]/h4/a 