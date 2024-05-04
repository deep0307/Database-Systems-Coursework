-- SQLite
-- In this question I first obtained Users having name "Taylor Swift" using like command.
-- Then I obtained the Channels created by this user through the WHERE command (stored it in tmp).
-- After obtaining the list of channels, I performed INNER JOIN on the Video table and the tmp table on the condition that video.channelID = tmp.channelID(stored it in tmp1)
-- After obtaining the Videos of the channels I wanted the Statistics information as it contained the comments column.
-- Thus I performed INNER JOIN on the Statistics table and tmp1 on the condition that Statistics.videoURL=tmp1.videoURL.
-- Now, since I wanted to obtain the most commented on video, I had to use the condition where comments = max commented video.
-- In order to achieve the goal mentioned above I used the max() function on the comments column.
-- Finally after obtaining the max commented video, I stored it in tmp2.
-- Then I obtained all the viewers of this max commented video by performing INNER JOIN on the Views table and tmp2 table on the Condition that Views.videoURL=tmp2.videoURL(stored it in tmp3).
-- Finally I performed INNER JOIN on the User table and tmp3 to obtain the User information.
-- Since the quesion requirement was to get the MaxAge and MinAge of the viewers I used the max() function and the min() function to obtain it.
-- Finally displayed all the information as per requirement of Q5 using the SELECT command.

SELECT tmp3.title, min(User.userAge) as MinAge,max(User.userAge) as MaxAge FROM User 
	INNER JOIN 
		(SELECT * from Views 
			INNER JOIN 
				(SELECT max(Statistics.comments) as MaxComments,Statistics.videoURL,title from Statistics 
					INNER JOIN (SELECT * from Video INNER JOIN (SELECT * from Channel where ownerID= 
						(SELECT userID FROM User where userName like '%Taylor Swift%')) 
					tmp ON Video.channelID=tmp.channelID) tmp1 ON Statistics.videoURL=tmp1.videoURL)
			tmp2 on Views.videoURL=tmp2.videoURL)
	tmp3 ON User.userID=tmp3.viewerID