import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
from collections import defaultdict
import csv
import re

sid = SentimentIntensityAnalyzer()

sentiments = []

#regex = re.compile(r'obama', flags=re.IGNORECASE) 

docs = ["politics2008.csv", "politics2009.csv", "politics2010.csv", "politics2011.csv", "politics2012.csv"]

for doc_path in docs:
    with open(doc_path, 'r') as file_reader:
        reader = csv.reader(file_reader, delimiter=',', quotechar='"')
        for row in reader:
			body = row[0].decode('utf-8')
			score = int(row[1])
			sentiment_values = []

			lines_list = tokenize.sent_tokenize(body)
			for sentence in lines_list:
				if "obama".upper() in sentence.upper():#(regex.search(sentence)):			
					s = sid.polarity_scores(sentence)
					sentiment_values.append(s['compound'])
			
			comment_sentiment = float(sum(sentiment_values))/len(sentiment_values)
			
			sentiments = sentiments + (score * [comment_sentiment])
	print sum(sentiments)/len(sentiments)