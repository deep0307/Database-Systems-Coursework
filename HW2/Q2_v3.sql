-- SQLite
-- In this question I changed the approach of joining the tables
-- Instead of going from Users table to Statistics table, I went in the backwards direction: Statistics table to User table. 
-- Instead of Using 3 INNER JOIN like Version 2 or using ownerID in (SELECT userID FROM User where userName LIKE '%Marvel Entertainment%'), I avoided it by going in the reverse direction
SELECT tmp2.title,tmp2.ChannelName,Ratio FROM User 
	INNER JOIN
		(SELECT tmp1.Ratio,tmp1.title,Channel.ownerID,Channel.ChannelName FROM Channel 
			INNER JOIN 
				(SELECT Video.title,tmp.Ratio,Video.channelID FROM Video 
					INNER JOIN 
						(SELECT (likes*1.0/nullif(viewCount,0)) as Ratio, videoURL from Statistics)
					tmp ON Video.videoURL=tmp.videoURL)
			tmp1 ON Channel.channelID=tmp1.channelID)
	tmp2 ON User.userID=tmp2.ownerID WHERE User.userName like '%Marvel Entertainment%' ORDER BY tmp2.title ASC
			