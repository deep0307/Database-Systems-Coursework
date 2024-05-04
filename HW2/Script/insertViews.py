# import pandas as pd
import random

# df=pd.read_csv('channels.csv')

with open("views.txt","w"):

    for i in range(1,10):
        vID=random.randint(1,1000)
        print('INSERT INTO "main"."Views" ("viewerID", "videoURL") VALUES (\''+str(vID)+'\',\''+"url"+str(56)+'\');',file=open("views.txt","a"))
    for i in range(1,10):
        vID=random.randint(1,1000)
        print('INSERT INTO "main"."Views" ("viewerID", "videoURL") VALUES (\''+str(vID)+'\',\''+"url"+str(2)+'\');',file=open("views.txt","a"))
    for i in range(1,10):
        vID=random.randint(1,1000)
        print('INSERT INTO "main"."Views" ("viewerID", "videoURL") VALUES (\''+str(vID)+'\',\''+"url"+str(1)+'\');',file=open("views.txt","a"))
    for i in range(1,971):
        vID=random.randint(1,1000)
        uID=random.randint(1,1000)
        print('INSERT INTO "main"."Views" ("viewerID", "videoURL") VALUES (\''+str(uID)+'\',\''+"url"+str(vID)+'\');',file=open("views.txt","a"))
