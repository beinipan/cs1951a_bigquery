from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import csv
import re

tokenizer = RegexpTokenizer(r'(?=\S[a-zA-Z\'-]+)([a-zA-Z\'-]+)')

# create English stop words list
en_stop = get_stop_words('en')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

doc_set = []
csvpath = '2013worldnews.csv'
csvpath2 = 'aww2016.csv'
csvpath3 = 'bigquery.csv'
with open(csvpath3, 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        doc_set.append(row[0].decode('utf-8')) 

# list for tokenized documents in loop
texts = []

# loop through document list
for i in doc_set:   
    # clean and tokenize document string
    raw = i.lower()
    raw = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', raw)
    raw = re.sub("^\d+\s|\s\d+\s|\s\d+$", " ", raw)
    raw = re.sub("&nbsp;", " ", raw)
    raw = re.sub("&lt;", " ", raw)
    raw = re.sub("&gt;", " ", raw)
    raw = re.sub("&amp;", " ", raw)
    raw = re.sub("&cent;", " ", raw)
    raw = re.sub("&pound;", " ", raw)
    raw = re.sub("&yen;", " ", raw)
    raw = re.sub("&euro;", " ", raw)
    raw = re.sub("&copy;", " ", raw)
    raw = re.sub("&reg;", " ", raw)
    tokens = tokenizer.tokenize(raw)

    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]
    
    # stem tokens
    # stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    
    # add tokens to list
    texts.append(stopped_tokens)

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)
    
# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=5, id2word = dictionary, passes=1)
# print(ldamodel[0])
for elem in ldamodel.print_topics(num_topics=5, num_words=5):
	print(elem)	