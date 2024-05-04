# import pandas as pd
import random

# df=pd.read_csv('channels.csv')

with open("statistics.txt","w"):

    for i in range(1,1001):
        views=random.randint(1,100000000)
        likes=random.randint(1,views)
        dislikes=random.randint(1,views)
        shares=random.randint(1,views)
        comments=random.randint(0,1000000)
        print('INSERT INTO "main"."Statistics" ("videoURL", "likes","dislikes", "views","shares","comments") VALUES (\''+"url"+str(i)+'\',\''+str(likes)+'\',\''+str(dislikes)+'\',\''+str(views)+'\',\''+str(shares)+'\',\''+str(comments)+'\');',file=open("statistics.txt","a"))
