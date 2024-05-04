-- SQLite
-- Please Note: Since I have considered February as the previous month as the submission is on the last day of the month. Morever I have considered the first 7 days as the first week for convenience and so on. The logic remains the same for all cases only the date ranges change.
-- First I obtain the users who reside in the US from the User table using the LIKE command(stored it in tmp).
-- Then I perform INNER JOIN on the Channel table and tmp table on the condition that Channel.ownerID = tmp.userID(stored it in tmp1).
-- Then I perform INNER JOIN on the Video table and tmp1 table on the condition that Video.channelID = tmp1.channelID
-- After performing the above INNER JOIN I added the where clause to obtain the videos that were uploaded in the first week of february.
-- I performed the above procedure 4 times (4 weeks in February) and managed the WHERE clauses accordingly.
-- Then I used the INTERSECT operation on all the 4 queries in order to obtain the information according to Q4.
-- Only those records will be displayed that satisfies all the 4 conditions; meaning the user has uploaded the video at least 1 time each week of February.

SELECT tmp1.userName,tmp1.ChannelName,tmp1.subscriptionCount FROM Video 
	INNER JOIN 
		(SELECT * FROM Channel 
			INNER JOIN 
				(SELECT * FROM User where userAddress="United States") 
			tmp ON Channel.ownerID=tmp.userID) 
	tmp1 ON Video.channelID=tmp1.channelID WHERE (Video.uploadTime>= "2023-02-01" AND Video.uploadTime<="2023-02-07") GROUP BY tmp1.channelID
INTERSECT 
SELECT tmp1.userName,tmp1.ChannelName,tmp1.subscriptionCount FROM Video 
	INNER JOIN 
		(SELECT * FROM Channel 
			INNER JOIN 
				(SELECT * FROM User where userAddress="United States") 
			tmp ON Channel.ownerID=tmp.userID) 
	tmp1 ON Video.channelID=tmp1.channelID WHERE (Video.uploadTime>= "2023-02-08" AND Video.uploadTime<="2023-02-14") GROUP BY tmp1.channelID
INTERSECT 
SELECT tmp1.userName,tmp1.ChannelName,tmp1.subscriptionCount FROM Video 
	INNER JOIN 
		(SELECT * FROM Channel 
			INNER JOIN 
				(SELECT * FROM User where userAddress="United States") 
			tmp ON Channel.ownerID=tmp.userID) 
	tmp1 ON Video.channelID=tmp1.channelID WHERE (Video.uploadTime>= "2023-02-15" AND Video.uploadTime<="2023-02-21") GROUP BY tmp1.channelID
INTERSECT 
SELECT tmp1.userName,tmp1.ChannelName,tmp1.subscriptionCount FROM Video 
	INNER JOIN 
		(SELECT * FROM Channel 
			INNER JOIN 
				(SELECT * FROM User where userAddress="United States") 
			tmp ON Channel.ownerID=tmp.userID) 
	tmp1 ON Video.channelID=tmp1.channelID WHERE (Video.uploadTime>= "2023-02-22" AND Video.uploadTime<="2023-02-28") GROUP BY tmp1.channelID
