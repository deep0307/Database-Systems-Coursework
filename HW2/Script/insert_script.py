# import pandas as pd
import random

# df=pd.read_csv('channels.csv')

with open("subscriptionQueries.txt","w"):
    for i in range(1,151):
        sID=random.randint(1,1000)
        print('INSERT INTO "main"."Subscription" ("subscriptionID", "channelID","subscriberID", "subscriptionType") VALUES (\''+str(i)+'\',\''+str(760)+'\',\''+str(sID)+'\',\'Paid\');',file=open("subscriptionQueries.txt","a"))

    for i in range(151,261):
        sID=random.randint(1,1000)
        print('INSERT INTO "main"."Subscription" ("subscriptionID", "channelID","subscriberID", "subscriptionType") VALUES (\''+str(i)+'\',\''+str(448)+'\',\''+str(sID)+'\',\'Paid\');',file=open("subscriptionQueries.txt","a"))

    for i in range(261,1001):
        chID=random.randint(1,1000)
        sID=random.randint(1,1000)
        lst=["Paid","Not Paid"]
        value=lst[random.randint(0,1)]
        print('INSERT INTO "main"."Subscription" ("subscriptionID", "channelID","subscriberID", "subscriptionType") VALUES (\''+str(i)+'\',\''+str(chID)+'\',\''+str(sID)+'\',\''+str(value)+'\');',file=open("subscriptionQueries.txt","a"))
