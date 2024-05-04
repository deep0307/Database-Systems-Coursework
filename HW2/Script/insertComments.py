# import pandas as pd
import random

# df=pd.read_csv('channels.csv')

with open("comments.txt","w"):

    sent=random.randint(1,100)
    uID=random.randint(1,1000)
    likes=random.randint(1,500)
    print('INSERT INTO "main"."Comment" ("videoURL","commentID","commenterID", "commentText","likes","sentiment") VALUES (\''+"url"+str(56)+'\',\''+str(1)+'\',\''+str(uID)+'\',\''+"comment"+str(1)+'\',\''+str(likes)+'\',\''+str(sent)+'\');',file=open("comments.txt","a"))

    sent=random.randint(1,100)
    uID=random.randint(1,1000)
    likes=random.randint(1,500)
    print('INSERT INTO "main"."Comment" ("videoURL","commentID","commenterID", "commentText","likes","sentiment") VALUES (\''+"url"+str(56)+'\',\''+str(2)+'\',\''+str(uID)+'\',\''+"comment"+str(2)+'\',\''+str(likes)+'\',\''+str(sent)+'\');',file=open("comments.txt","a"))

    sent=random.randint(1,100)
    uID=random.randint(1,1000)
    likes=random.randint(1,500)
    print('INSERT INTO "main"."Comment" ("videoURL","commentID","commenterID", "commentText","likes","sentiment") VALUES (\''+"url"+str(56)+'\',\''+str(3)+'\',\''+str(uID)+'\',\''+"comment"+str(3)+'\',\''+str(likes)+'\',\''+str(sent)+'\');',file=open("comments.txt","a"))

    sent=random.randint(1,100)
    uID=random.randint(1,1000)
    likes=random.randint(1,500)
    print('INSERT INTO "main"."Comment" ("videoURL","commentID","commenterID", "commentText","likes","sentiment") VALUES (\''+"url"+str(56)+'\',\''+str(4)+'\',\''+str(uID)+'\',\''+"comment"+str(4)+'\',\''+str(likes)+'\',\''+str(sent)+'\');',file=open("comments.txt","a"))

    sent=random.randint(1,100)
    uID=random.randint(1,1000)
    likes=random.randint(1,500)
    print('INSERT INTO "main"."Comment" ("videoURL","commentID","commenterID", "commentText","likes","sentiment") VALUES (\''+"url"+str(2)+'\',\''+str(5)+'\',\''+str(uID)+'\',\''+"comment"+str(5)+'\',\''+str(likes)+'\',\''+str(sent)+'\');',file=open("comments.txt","a"))

    sent=random.randint(1,100)
    uID=random.randint(1,1000)
    likes=random.randint(1,500)
    print('INSERT INTO "main"."Comment" ("videoURL","commentID","commenterID", "commentText","likes","sentiment") VALUES (\''+"url"+str(2)+'\',\''+str(6)+'\',\''+str(uID)+'\',\''+"comment"+str(6)+'\',\''+str(likes)+'\',\''+str(sent)+'\');',file=open("comments.txt","a"))

    sent=random.randint(1,100)
    uID=random.randint(1,1000)
    likes=random.randint(1,500)
    print('INSERT INTO "main"."Comment" ("videoURL","commentID","commenterID", "commentText","likes","sentiment") VALUES (\''+"url"+str(2)+'\',\''+str(7)+'\',\''+str(uID)+'\',\''+"comment"+str(7)+'\',\''+str(likes)+'\',\''+str(sent)+'\');',file=open("comments.txt","a"))


    for i in range(8,1001):
        urlID=random.randint(1,1000)
        sent=random.randint(1,100)
        uID=random.randint(1,1000)
        likes=random.randint(1,500)
        print('INSERT INTO "main"."Comment" ("videoURL","commentID","commenterID", "commentText","likes","sentiment") VALUES (\''+"url"+str(urlID)+'\',\''+str(i)+'\',\''+str(uID)+'\',\''+"comment"+str(i)+'\',\''+str(likes)+'\',\''+str(sent)+'\');',file=open("comments.txt","a"))
