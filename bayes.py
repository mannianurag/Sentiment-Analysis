# import nltk
#
# with open ("D:/sentiment/pos.review", "r") as myfile:
#     data=myfile.readlines()
#
# arr=[]
# for word in data:
#     word=word.replace("\n",'')
#     ele=(word,'positive')
#     arr.append(ele)
#     # print(ele)
#
# pos_tweets=arr
#
# with open("D:/sentiment/neg.review", "r") as myfile:
#     data = myfile.readlines()
# arr = []
# for word in data:
#     word = word.replace("\n", '')
#     ele = (word, 'negative')
#     arr.append(ele)
#     # print(ele)
#
# neg_tweets = arr
#

# for (words, sentiment) in pos_tweets + neg_tweets:
#     words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
#     tweets.append((words_filtered, sentiment))
# #
# # test_tweets = [
# #     (['feel', 'happy', 'this', 'morning'], 'positive'),
# #     (['larry', 'friend'], 'positive'),
# #     (['not', 'like', 'that', 'man'], 'negative'),
# #     (['house', 'not', 'great'], 'negative'),
# #     (['your', 'song', 'annoying'], 'negative')]
#
#

tweets = []
def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
        all_words.extend(words)
    return all_words


import nltk

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

word_features = get_word_features(get_words_in_tweets(tweets))

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


def bayesFunc(string):
    import pickle
    f = open('D:/sentiment/bayes_classifier.pickle', 'rb')
    #f = open('bayes_classifier.pickle', 'rb')
    classifier = pickle.load(f)
    f.close()
    tweet=string
    return(classifier.classify(extract_features(tweet.split())))




