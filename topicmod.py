#example i found online, only problem is we have to make the vocab list? or something, or we can use a count vectorizer thing i guess? 

import numpy as np
import lda
import lda.datasets

X = lda.datasets.load_reuters()
vocab = lda.datasets.load_reuters_vocab()

print "x"
print X

print "vocab"
print vocab[0]

model = lda.LDA(n_topics=20, n_iter=1500, random_state=1)
model.fit(X)  # model.fit_transform(X) is also available
topic_word = model.topic_word_  # model.components_ also works
n_top_words = 8
for i, topic_dist in enumerate(topic_word):
	topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
	print('Topic {}: {}'.format(i, ' '.join(topic_words)))