import stopWords
from bayes import bayesFunc
from duplicate import duplicate
from notRemoverStart import notRemoverfunc
import csv

from rating import calcRating
def start(string):
    tweet = string
    #print("tweet :", tweet)
    tweet = duplicate(tweet)
    #print("tweet :", tweet)
    tweet = stopWords.stopWordsFunc(tweet)
    #print("tweet :", tweet)
    tweet = (notRemoverfunc(tweet))
    #print("tweet :", tweet)
    (bayesFunc(tweet))

    rating = calcRating(tweet)
    return rating

print("---")
file=open("D:\sentiment\ip_to_exe.txt")
review = file.readline()

rating=str(start(review))
file=open("D:\sentiment\op_from_exe.txt",'w')
file.writelines(rating)

with open("D://sentiment/all_ratings.csv",'a',newline='\n') as fp:
    a=csv.writer(fp,delimiter=',')
    data=[[review,rating]]
    a.writerows(data)
    print("completed")
