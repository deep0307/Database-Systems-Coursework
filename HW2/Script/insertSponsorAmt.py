# import pandas as pd
import random

# df=pd.read_csv('channels.csv')

with open("sponsorAmt.txt","w"):

    for i in range(1,1001):
        amt=random.randint(1,100000)
        sponsorID=random.randint(1,100)
        print('INSERT INTO "main"."SponsoringVideo" ("sponsorID", "videoURL","sponsorAmount") VALUES (\''+str(sponsorID)+'\',\''+"url"+str(i)+'\',\''+str(amt)+'\');',file=open("sponsorAmt.txt","a"))
