import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer



class Tokenizer():
    def __init__(self, language, community):
        #nltk.download('stopwords')
        self.stopwords = stopwords.words(language)
        self.stopwords.extend(['date', 'dates', 'month', 'months', 'year', 'years'])
        self.community = community
        if self.community == "fool":
            self.ad_sentence = ["Before you consider Exxon Mobil Corporation, you'll want to hear this.", 
            "Investing legends and Motley Fool Co-founders David and Tom Gardner just revealed what they believe are the 10 best stocks for investors to buy right now... and Exxon Mobil Corporation wasn't one of them.", 
            "The online investing service they've run for nearly two decades, Motley Fool Stock Advisor, has beaten the stock market by over 4X.", 
            "* And right now, they think there are 10 stocks that are better buys.", 
            "The online investing service they've run for nearly two decades, Motley Fool Stock Advisor, has beaten the stock market by over 4X.* And right now, they think there are 10 stocks that are better buys.",
            "See the 10 stocks", 
            "*Stock Advisor returns as of February 24, 2021",
            "IMAGE SOURCE: GETTY IMAGES."]

            self.path = "../community_crawler/fool.com/articles/"
            self.save_path = "fool.com/"

    def tokenize_article(self):
        self.file_list = os.listdir(self.path)
        for file_name in self.file_list:
            tokenize_paragraph = self.tokenize(file_name)
            with open(self.save_path + file_name, 'w') as f:
                for tokenize_sentence in tokenize_paragraph:
                    for tokenize_word in tokenize_sentence:
                        f.write(tokenize_word + ', ')
                    f.write('\n')
                


    def tokenize(self, file_name):
        result = []
        with open(self.path + file_name, 'r') as f:
            article = f.readlines()
            for sentence in article:
                if len(sentence[:-1]) < 1 or sentence[:-1] in self.ad_sentence:
                    continue

                #print("sentence: {sentence}".format(sentence=sentence[:-1]))
                #print("tokenize sentence: {token}".format(token=WordPunctTokenizer().tokenize(sentence)))
                #new_token = [t for t in token if not t in self.stopwords]
                #print("new_token: {new_token}".format(new_token=new_token))
                #print()
                token = WordPunctTokenizer().tokenize(sentence)
                result.append([t for t in token if (not t in self.stopwords) and t.isalnum()])

        return result

if __name__ == "__main__":
    tokenizer = Tokenizer('english', 'fool')
    tokenizer.tokenize_article()