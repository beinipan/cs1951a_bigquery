from textstat.textstat import textstat
import re
import time
import csv

start_time = time.time()

def load_file(file_path):
    comments = []
    with open(file_path, 'r') as file_reader:
        reader = csv.reader(file_reader, delimiter=',', quotechar='"')
        reader.next()
        for row in reader:
            text = re.sub('([A-Za-z]+:\/\/[A-Za-z0-9]+\.[A-Za-z0-9]+[^\s-]*)|([A-Za-z]+\.[A-Za-z0-9]+\.[A-Za-z0-9]+[^\s-]*)', '', row[0]) #url get rid
            text = re.sub('\s\s+', ' ', text)
            comments.append(text)
    return comments

docs = ["AskReddit2008.csv", "AskReddit2009.csv", "AskReddit2010.csv", "AskReddit2011.csv", "AskReddit2012.csv", "AskReddit2013.csv", "AskReddit2014.csv"]

for doc_path in docs:
	documents = load_file(doc_path)
	levels = [textstat.flesch_reading_ease(comment) for comment in documents if textstat.sentence_count(comment) != 0]
	print "reading level for " + doc_path
	print sum(levels)/len(levels)

elapsed_time = time.time() - start_time
print "elapsed time in seconds: " + str(elapsed_time)