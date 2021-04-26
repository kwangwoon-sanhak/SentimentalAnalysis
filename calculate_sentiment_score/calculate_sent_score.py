import os
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
from afinn import Afinn

class VocabDictionary:
    def __init__(self, vocab_name):
        super().__init__()
        self.vocab_name = vocab_name
        self.file_path = "../toknizer/fool.com/"

    def sentiment_analysis(self):
        self.file_list = os.listdir(self.file_path)
        for file_name in self.file_list:
            with open(self.file_path + file_name, 'r') as f:
                paragraph = f.readlines()
                line_number = len(paragraph)
                score = self.calculate_score(paragraph)
                #평균낼지 합을 출력할건지 결정 평균은 line_number로 나누면된다.
                print("".format())
                
    def calculate_score(self, paragraph):
        sentimental_score = {'pos': 0, 'neu': 0, 'neg': 0, 'compound'}
        if self.vocab_name == "VADER":
            for sentence in paragraph:
                score = self.calculate_score_with_vader(sentence)
                #print("'{sentence}'s score is {score}".format(sentence=sentence, score=score))
                #score를 sentimental score에 더해주자
            #그리고 sentimental score를 리턴
        if self.vocab_name == "AFINN":
            pass

        if self.vocab_name == "TextBlob":
            pass

        if not self.vocab_name in ["VADER", "AFINN", "TextBlob"]:
            return None
    
    def calculate_score_with_vader(self, sentence):
        analyzer = SentimentIntensityAnalyzer()
        score = analyzer.polarity_scores(sentence)
        return score

    def calculate_score_with_afinn(self, paragraph):
        pass

    def calculate_score_with_textblob(self, paragraph):
        pass

if __name__ == "__main__":
    vocab_dic = VocabDictionary("VADER")
    vocab_dic.sentiment_analysis()