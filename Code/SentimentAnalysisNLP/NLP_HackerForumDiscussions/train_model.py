'''
train_model.py
@author: jubinsoni
Text analysis, Sentiment Analysis
'''

import nltk
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
import re, csv, sys
from unidecode import unidecode

reload(sys)
sys.setdefaultencoding('utf8')

spchars = re.compile('\`|\~|\!|\@|\#|\$|\%|\^|\&|\*|\(|\)|\_|\+|\=|\\|\||\{|\[|\]|\}|\:|\;|\'|\"|\<|\,|\>|\?|\/|\.|\-')


# Utility function that does the following to the text:
# - Convert to unicode
# - Convert to lowercase
# - Remove special chars
def make_text_parsable(text):
    # convert text to lowercase
    text = text.lower()
    # convert text to unicode
    text = text.decode('windows-1252')
    # remove special characters
    text = spchars.sub(" ", text)
    return (text)


def word_feats(words, sentiment):
    return dict([(word, sentiment) for word in words])

def format_data(negfile, posfile):
    negids = nltk.word_tokenize(make_text_parsable(open(negfile).read().lower()))
    posids = nltk.word_tokenize(make_text_parsable(open(posfile).read().lower()))
    negfeats = word_feats(negids, 'neg')
    posfeats = word_feats(posids, 'pos')

    with open('train-utf8.csv', 'wb') as output_csv:
        writer = csv.writer(output_csv)
        for row in negfeats.iteritems():
            writer.writerow(row)
        for row in posfeats.items():
            writer.writerow(row)
        output_csv.close()


def train_sentiment_model(data_file):
    train = pd.read_csv(data_file)
    vectorizer = TfidfVectorizer(min_df=1, ngram_range=(1, 10))
    X_train = vectorizer.fit_transform(train.word)
    model = MultinomialNB().fit(X_train, list(train.sentiment))
    return model, vectorizer


def get_prob_of_sentiment(text, vec, model):
    test = vec.transform([text])
    return model.predict_proba(test)[0][1]


def get_sentiment(text):
    data_file = 'train-utf8.csv'
    model, vectorizer = train_sentiment_model(data_file)
    test = vectorizer.transform([text])
    return model.predict(test)


if __name__ == '__main__':
    # format_data('negativeWords.txt', 'positiveWords.txt') #converts positive negative words into one csv for training
	# print model.predict_proba(test)
    #input = "good movie I like it"
	#For single input the code tkae miliseconds, for big files its intensive

	input_file = pd.read_csv("MRinputposts_inputFile.csv") #Enter your filename here
	output_file = csv.writer(open('sentiment_output.csv', 'wb')) #Output is saved is just 'pos' or 'neg'
	print "Starting sentiment analysis..."
	d = {}
	for input in input_file.threadTitle: #Instead of Comments change the column where in file there are comments
		d[input] = get_sentiment(str(input)) #Comment this if you dont want to see the output
		output_file.writerow(get_sentiment(str(input)))
	print "Complete."
	print d #Comment this if you dont want to see the output


