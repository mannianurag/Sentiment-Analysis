from nltk.corpus import stopwords

def stopWordsFunc(sentence):
    # sentence = "this is not only a very bad phone"
    stop = set(stopwords.words('english'))
    # stop = set(stopwords) - operators
    tweet= ([i for i in sentence.lower().split()
            if i not in stop or i == 'not' or i == 'very'])

    string = ' '.join(tweet)
    return(string)

