# import pandas as pd
import random

# df=pd.read_csv('channels.csv')

with open("infoView.txt","w"):

    keywords=["keyword1","keyword2","keyword3","keywords4","keywords5"]
    for i in range(1,1001):
        if(i%2==0):
            for j in range(0,5):
                if random.random()>0.5:
                    print('INSERT INTO "main"."InfoVideo" ("videoURL", "keywords") VALUES (\''+"url"+str(i)+'\',\''+str(keywords[j])+'\');',file=open("infoView.txt","a"))
