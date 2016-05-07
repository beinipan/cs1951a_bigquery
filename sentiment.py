import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
from collections import defaultdict
import csv
import re

sid = SentimentIntensityAnalyzer()

subreddit_sentiments = defaultdict(list)
subreddit_total = defaultdict(int)

filepath = "dank2.csv"

#regex = re.compile(r'obama', flags=re.IGNORECASE) 

with open(filepath) as f:
	reader = csv.reader(f)
	reader.next()

	for row in reader:
		body = row[1].decode('utf-8')
		score = row[2]
		sentiment_values = []
		lines_list = tokenize.sent_tokenize(body)
		for sentence in lines_list:
			if "dank".upper() in sentence.upper():#(regex.search(sentence)):			
				s = sid.polarity_scores(sentence)
				sentiment_values.append(s['compound'])
		
		comment_sentiment = float(sum(sentiment_values))/len(sentiment_values)
		subreddit_sentiments[row[0]].append((comment_sentiment, score))
		subreddit_total[row[0]] += int(score)

subreddit_sentiments = {subreddit:float(sum([float(pair[0])*float(pair[1]) for pair in sentiment_list]))/subreddit_total[subreddit] for subreddit, sentiment_list in subreddit_sentiments.items()}
print sorted(subreddit_sentiments.items(), key = lambda(k,v): (-v,k))