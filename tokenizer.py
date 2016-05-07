from porter_stemmer import PorterStemmer
import re
import string

class Tokenizer(object):
    def __init__(self):
        self.stemmer = PorterStemmer()

    # only admit non-number with length>2
    def qualify(self, word):
        return len(word)>2 and not word.isdigit()

    # TODO: Change the text processing here
    # You only need to edit the below function
    def process_tweet(self, tweet):
        tweet = tweet.lower()
        exclude = set(string.punctuation)
        tweet = ''.join(ch for ch in tweet if ch not in exclude)
        words = tweet.split()

        for i in range(len(words)):
            words[i] = self.stemmer.stem(words[i], 0, len(words[i]) - 1)
        
        tweet = ' '.join(words)
        return tweet

    def __call__(self, tweet):
        # This function takes in a single tweet (just the text part)
        # then it will process/clean the tweet and return a list of tokens (words).
        # For example, if tweet was 'I eat', the function returns ['i', 'eat']

        # You will not need to call this function explictly.
        # Once you initialize your vectorizer with this tokenizer,
        # then 'vectorizer.fit_transform()' will implictly call this function to
        # extract features from the training set, which is a list of tweet texts.
        # So once you call 'fit_transform()', the '__call__' function will be applied
        # on each tweet text in the training set (a list of tweet texts),
        features = []
        for word in self.process_tweet(tweet).split():
            if self.qualify(word):
                # Stem
                word = self.stemmer.stem(word, 0, len(word) - 1)

                features.append(word)

        return features
