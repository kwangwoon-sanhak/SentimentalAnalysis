import os
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
from afinn import Afinn

class VocabDictionary:
    def __init__(self, vocab_name, ticker):
        super().__init__()
        self.vocab_name = vocab_name
        ticker_list ["XOM", "CVX", "XEC", "HES"]
        #XOM : ../toknizer/fool.com/XOM
        #CVX : ../toknizer/fool.com/CVX
        #XEC : ../toknizer/fool.com/XEC
        #HES : ../toknizer/fool.com/HES
        if ticker = "XOM":
            self.file_path = os.path.join(os.path.dirname(__file__), "../toknizer/fool.com/XOM")
        if ticker = "CVX":
            self.file_path = os.path.join(os.path.dirname(__file__), "../toknizer/fool.com/CVX")
        if ticker = "XEC":
            self.file_path = os.path.join(os.path.dirname(__file__), "../toknizer/fool.com/XEC")
        if ticker = "HES":
            self.file_path = os.path.join(os.path.dirname(__file__), "../toknizer/fool.com/HES")

        if not ticker in ticker_list:
            print("종목이 없습니다.")
            exit(0)
        

    def sentiment_analysis(self):
        self.file_list = os.listdir(self.file_path)
        sent_score_dict = {}
        pos_score_dict = {}
        neu_score_dict = {}
        neg_score_dict = {}
        compound_score_dict = {}

        for file_name in self.file_list:

            if '_' in file_name:
                date = file_name.split('_')[1].split('.')[0]
            else:
                continue

            with open(self.file_path + file_name, 'r') as f:
                paragraph = f.readlines()
                self.line_number = len(paragraph)
                if self.line_number == 0:
                    continue
                score = self.calculate_score(paragraph)
                pos_score_dict[date] = score['pos']
                neu_score_dict[date] = score['neu']
                neg_score_dict[date] = score['neg']
                compound_score_dict[date] = score['compound']
            
        sent_score_dict['pos'] = pos_score_dict
        sent_score_dict['neu'] = neu_score_dict
        sent_score_dict['neg'] = neg_score_dict
        sent_score_dict['compound'] = compound_score_dict

        return sent_score_dict
                #평균낼지 합을 출력할건지 결정 평균은 line_number로 나누면된다.
                #print("".format())
                
    def calculate_score(self, paragraph):
        sentimental_score = []
        sent_score_dict = {'pos': 0, 'neu': 0, 'neg': 0, 'compound': 0}
        if self.vocab_name == "VADER":
            for sentence in paragraph:
                score = self.calculate_score_with_vader(sentence)
                if score['compound'] == 0:
                    self.line_number -= 1
                    continue
                if score['compound'] != 0:
                    sentimental_score.append(score)

            sent_score_dict['pos'] = round(sum(score['pos'] for score in sentimental_score) / self.line_number, 4)
            sent_score_dict['neu'] = round(sum(score['neu'] for score in sentimental_score) / self.line_number, 4)
            sent_score_dict['neg'] = round(sum(score['neg'] for score in sentimental_score) / self.line_number, 4)
            sent_score_dict['compound'] = round(sum(score['compound'] for score in sentimental_score) / self.line_number, 4)

            return sent_score_dict
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
    vocab_dic = VocabDictionary("VADER", "XOM")
    score = vocab_dic.sentiment_analysis()
    print(score['pos'])
    print(score['neu'])
    print(score['neg'])
    print(score['compound'])