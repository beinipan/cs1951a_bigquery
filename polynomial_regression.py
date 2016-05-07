from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
from tokenizer import Tokenizer
from sklearn.feature_extraction.text import CountVectorizer
import csv
from sklearn.linear_model import LogisticRegression
import util
import numpy

from sklearn.linear_model import SGDRegressor

def load_file(file_path):
    karma = []
    comments = []
    with open(file_path, 'r') as file_reader:
        reader = csv.reader(file_reader, delimiter=',', quotechar='"')
        reader.next()
        for row in reader:
            score = int(row[1])
            text = row[0]
            karma.append(score)
            comments.append(text)
    return (karma, comments)

tokenizer = Tokenizer()
vectorizer = CountVectorizer(binary=True, lowercase=True, decode_error='replace', tokenizer=tokenizer)
(training_labels1, training_texts1) = load_file("trainHighScore.csv")
(training_labels2, training_texts2) = load_file("trainMidScore.csv")
(training_labels3, training_texts3) = load_file("trainMidHighScore.csv")
(training_labels4, training_texts4) = load_file("trainLowScore.csv")

training_labels = training_labels1 + training_labels2 + training_labels3# + training_labels4
training_texts = training_texts1 + training_texts2 + training_texts3# + training_texts4

training_features = vectorizer.fit_transform(training_texts)
training_labels = numpy.array(training_labels)

classifier = LogisticRegression()
classifier.fit(training_features, training_labels)

(testing_labels, testing_texts) = load_file("train2.csv")

test_features = vectorizer.transform(testing_texts)

print("Prediction = ", classifier.predict(test_features))
print(testing_labels)

util.print_most_informative_features('log', vectorizer, classifier, n=10)