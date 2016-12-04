from nltk.corpus import wordnet as wn
def opp(str):
    good = wn.synset(str+".a.01")
    var=good.lemmas()[0].antonyms()
    return(var)
