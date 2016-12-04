import math
import nltk


def calcRating(string):

    #positive words
    import csv
    wordlist=list()
    #with open('pos.csv', 'r') as f:
    with open('D:/sentiment/pos.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            wordlist.append(row)  #make a list of csv rows
        #print("wordlist = ",wordlist)
    total=int()
    for i in range(len(wordlist)):
        total+=int(wordlist[i][0])  #calculate total
    #print("total=",total)

    rating_pos=1
    count_pos=0
    tokenizedString = nltk.word_tokenize(string)
    #print("tokenized string = ",tokenizedString)
    for i in range(len(tokenizedString)):
        for j in range(len(wordlist)):
            if(tokenizedString[i]) in wordlist[j][1]:
                #print("r= ",rating_pos, "for ",wordlist[j][1]," with ",(wordlist[j][0]))
                count_pos+=1
                rating_pos=rating_pos*(int(wordlist[j][0])/total)

    #print("rating_pos = ",rating_pos,"  count", count_pos)
    #print("------------------------------------------------------")








    total_neg=0
    count_neg = 0
    wordlist_neg = list()
    #with open('neg.csv', 'r') as f:
    with open('D:/sentiment/neg.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            wordlist_neg.append(row)  #make a list of csv rows
        #print("wordlist_neg = ",wordlist_neg)
    total_neg=int()
    for i in range(len(wordlist_neg)):
        total_neg+=int(wordlist_neg[i][0])  #calculate total_neg
    #print("total_neg=",total_neg)

    rating_neg=1
    #print("tokenized string = ",tokenizedString)
    for i in range(len(tokenizedString)):
        for j in range(len(wordlist_neg)):
            if(tokenizedString[i]) in wordlist_neg[j][1]:
                #print("r= ",rating_neg, "for ",wordlist_neg[j][1]," with ",(wordlist_neg[j][0]))
                count_neg+=1
                rating_neg=rating_neg*(int(wordlist_neg[j][0])/total_neg)

    #print("rating_neg = ",rating_neg,"  count ",count_neg)


    pos_r=(math.pow(total_neg,count_pos))*rating_pos
    neg_r =(math.pow(total, count_neg))*rating_neg


    pos=pos_r/(pos_r+neg_r)*5
    neg=neg_r/(neg_r+pos_r)*5
    #print("Positve Rating:", pos, " Negative Rating:", neg)
    finalRating=''
    if pos>neg:
        print("Final Rating: ",pos)
        finalRating = 'positive'
        print(finalRating)
        return(pos)


    elif pos<neg:
        print("Final Rating: ",5-neg)
        finalRating = 'negative'
        print(finalRating)
        return (5-neg)


    else: #equal
        finalRating = 'neutral'
        #print("Final Rating:", pos)
        print(finalRating)
        return (2.5)

    # print("Sentiment: ",finalRating)

# calcRating("bad poor")