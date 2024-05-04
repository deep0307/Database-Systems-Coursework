# import pandas as pd
import random
from randomtimestamp import randomtimestamp

# df=pd.read_csv('channels.csv')

with open("Video.txt","w"):

    lst=["Horror","Thriller","Comedy","Sci-Fi","Romantic"]
    value=lst[random.randint(1,len(lst)-1)]
    time=random.randint(0,40)/10
    print('INSERT INTO "main"."Video" ("channelID", "videoURL","title", "thumbnail","category","description","duration","uploadTime") VALUES (\''+str(239)+'\',\''+"url"+str(1)+'\',\''+"title"+str(1)+'\',\''+"thumbnail"+str(1)+'\',\''+value+'\',\''+"description"+str(1)+'\',\''+str(time)+'\',\'2023-02-01 23:59:59\');',file=open("Video.txt","a"))

    value=lst[random.randint(1,len(lst)-1)]
    time=random.randint(0,40)/10
    print('INSERT INTO "main"."Video" ("channelID", "videoURL","title", "thumbnail","category","description","duration","uploadTime") VALUES (\''+str(239)+'\',\''+"url"+str(2)+'\',\''+"title"+str(2)+'\',\''+"thumbnail"+str(2)+'\',\''+value+'\',\''+"description"+str(2)+'\',\''+str(time)+'\',\'2023-02-08 23:59:59\');',file=open("Video.txt","a"))

    value=lst[random.randint(1,len(lst)-1)]
    time=random.randint(0,40)/10
    print('INSERT INTO "main"."Video" ("channelID", "videoURL","title", "thumbnail","category","description","duration","uploadTime") VALUES (\''+str(239)+'\',\''+"url"+str(3)+'\',\''+"title"+str(3)+'\',\''+"thumbnail"+str(3)+'\',\''+value+'\',\''+"description"+str(3)+'\',\''+str(time)+'\',\'2023-02-15 23:59:59\');',file=open("Video.txt","a"))

    value=lst[random.randint(1,len(lst)-1)]
    time=random.randint(0,40)/10
    print('INSERT INTO "main"."Video" ("channelID", "videoURL","title", "thumbnail","category","description","duration","uploadTime") VALUES (\''+str(239)+'\',\''+"url"+str(4)+'\',\''+"title"+str(4)+'\',\''+"thumbnail"+str(4)+'\',\''+value+'\',\''+"description"+str(4)+'\',\''+str(time)+'\',\'2023-02-22 23:59:59\');',file=open("Video.txt","a"))

    value=lst[random.randint(1,len(lst)-1)]
    time=random.randint(0,40)/10
    print('INSERT INTO "main"."Video" ("channelID", "videoURL","title", "thumbnail","category","description","duration","uploadTime") VALUES (\''+str(811)+'\',\''+"url"+str(5)+'\',\''+"title"+str(5)+'\',\''+"thumbnail"+str(5)+'\',\''+value+'\',\''+"description"+str(5)+'\',\''+str(time)+'\',\'2023-02-02 23:59:59\');',file=open("Video.txt","a"))

    value=lst[random.randint(1,len(lst)-1)]
    time=random.randint(0,40)/10
    print('INSERT INTO "main"."Video" ("channelID", "videoURL","title", "thumbnail","category","description","duration","uploadTime") VALUES (\''+str(811)+'\',\''+"url"+str(6)+'\',\''+"title"+str(6)+'\',\''+"thumbnail"+str(6)+'\',\''+value+'\',\''+"description"+str(6)+'\',\''+str(time)+'\',\'2023-02-09 23:59:59\');',file=open("Video.txt","a"))

    value=lst[random.randint(1,len(lst)-1)]
    time=random.randint(0,40)/10
    print('INSERT INTO "main"."Video" ("channelID", "videoURL","title", "thumbnail","category","description","duration","uploadTime") VALUES (\''+str(811)+'\',\''+"url"+str(7)+'\',\''+"title"+str(7)+'\',\''+"thumbnail"+str(7)+'\',\''+value+'\',\''+"description"+str(7)+'\',\''+str(time)+'\',\'2023-02-16 23:59:59\');',file=open("Video.txt","a"))

    value=lst[random.randint(1,len(lst)-1)]
    time=random.randint(0,40)/10
    print('INSERT INTO "main"."Video" ("channelID", "videoURL","title", "thumbnail","category","description","duration","uploadTime") VALUES (\''+str(811)+'\',\''+"url"+str(8)+'\',\''+"title"+str(8)+'\',\''+"thumbnail"+str(8)+'\',\''+value+'\',\''+"description"+str(8)+'\',\''+str(time)+'\',\'2023-02-23 23:59:59\');',file=open("Video.txt","a"))


    for i in range(9,1001):
        chID=random.randint(1,1000) 
        timestamp=str(randomtimestamp(start_year=2022,end_year=2023))
        value=lst[random.randint(1,len(lst)-1)]
        time=random.randint(0,40)/10
        print('INSERT INTO "main"."Video" ("channelID", "videoURL","title", "thumbnail","category","description","duration","uploadTime") VALUES (\''+str(chID)+'\',\''+"url"+str(i)+'\',\''+"title"+str(i)+'\',\''+"thumbnail"+str(i)+'\',\''+value+'\',\''+"description"+str(i)+'\',\''+str(time)+'\',\''+timestamp+'\');',file=open("Video.txt","a"))
