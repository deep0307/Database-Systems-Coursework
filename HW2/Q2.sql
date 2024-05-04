-- SQLite
-- In this query I first obtained the list of userID's of the users that have the name - "Marvel Entertainment" in them using LIKE command.
-- I then obtained the list of channels which were owned by the userID's obtained above (stored in tmp).
-- Then I performed INNER JOIN on the Video table and the Channel table obtained from above on the condition that Video.channelID=tmp.channelID (stored in tmp1).
-- After this I again performed INNER JOIN on Statistics and the table obtained from above on the condition that Statistics.videoURL=tmp1.videoURL
-- Before displaying the information required, the Q2, required to order the information based on the ascending order of the video title. So I used ORDER BY title ASC to achieve that.
-- Finally I displayed all the information required- tmp1.title,tmp1.ChannelName and the ratio of likes and viewCount. For the ratio I multiplied by 1.0 in order to recieve a decimal ratio, otherwise it gives output as 0 since it treats the values as integers.

SELECT tmp1.title,tmp1.ChannelName,(Statistics.likes*1.0/nullif(Statistics.viewCount,0)) as Ratio from Statistics 
	INNER JOIN 
		(SELECT * from Video 
			INNER JOIN 
				(SELECT * FROM Channel where ownerID IN (SELECT userID FROM User where userName LIKE '%Marvel Entertainment%'))
			tmp ON Video.channelID=tmp.channelID)
	tmp1 ON Statistics.videoURL= tmp1.videoURL ORDER BY tmp1.title ASC