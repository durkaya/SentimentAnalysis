from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from textblob import Word, TextBlob


def lemmatize_process(word):
    w = Word(word)
    w.lemmatize()
    return w


def stem_process(word):
    grouping = PorterStemmer()
    grouping.stem(word)


def tokenize_process(tweet_id, tweet):
    fs = open("tokenize.txt", "a")
    lemmatized = []
    tokens = word_tokenize(tweet)
    for index in range(len(tokens)):
        lemmatized.append(lemmatize_process(tokens[index]))

    fs.write('id: ' + tweet_id + '{ ')
    fs.write(str(lemmatized))
    fs.write(' }\n\n')
    print(lemmatized)
    fs.close()


def sample_analysis(tweet):
    sample = TextBlob(tweet)
    print(sample.sentiment, '\n')
