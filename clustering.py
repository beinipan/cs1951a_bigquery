# from sklearn.feature_extraction.text import TfidfVectorizer

# tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=200000,
#                                  min_df=0.2, stop_words='english',
#                                  use_idf=True, tokenizer=tokenize_and_stem, ngram_range=(1,3))

# tfidf_matrix = tfidf_vectorizer.fit_transform(synopses)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import csv
import time
import re

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

documents = load_file("aww2016.csv")
true_k = 6

vectorizer = TfidfVectorizer(stop_words='english', max_features=200000, use_idf=True, ngram_range=(1,3))
X = vectorizer.fit_transform(documents)
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=500, n_init=1)
model.fit(X)
print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print "Cluster %d:" % i,
    for ind in order_centroids[i, :15]:
        print ' %s' % terms[ind].encode('utf-8'),
    print

elapsed_time = time.time() - start_time
print "elapsed time in seconds: " + str(elapsed_time)

