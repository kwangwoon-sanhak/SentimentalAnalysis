# SentimentalAnalysis

##필요한 모듈 설치 :
###selenium
https://github.com/SeleniumHQ/selenium

###nltk
https://github.com/nltk/nltk

###vader
https://github.com/cjhutto/vaderSentiment

##comminity_crawler/fool.com/fool_crawler.py 는 fool 사이트의 각 종목에 따른 레포트 문장들을 크롤링하는 파일
###해당 종목의 url을 url 변수에 대입하고, 모든 레포트의 url을 얻어 txt파일로 저장하는 것은 PHASE[1], txt 파일의 모든 url의 레포트 문장들을 크롤링하는 것은 PHASE[2]로 current_phase 변수에 저장하여 실행

##tokenizer/nltk_tokenizer.py 는 크롤링한 레포트 문장들을 불용어 제거 및 토크나이징 하는 파일
###토크나이징할 문장의 언어와, 사이트 이름을 넣으면 해당 사이트의 크롤링 문장들의 불용어를 제거하고 토크나이징한 결과를 txt 파일로 저장함

##calculate_sentiment_score/calculate_sentiment_score.py는 토크나이징한 단어들을 문장별로 감성 점수를 계산하고, 문단 별로 감성 점수를 평균내는 파일
###사용하려는 감성어 사전을 객체로 생성하여 sentiment_analysis 메소드를 실행하면 해당 문장의 긍정, 중립, 긍정, 총계 점수가 출력된다.
