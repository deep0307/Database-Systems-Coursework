-- SQLite
-- For this question I changed the approach.
-- Instead of picking the ownerID from userID table, I decided to perform INNER JOIN with the table. Rest of the query remains unchanged

SELECT tmp2.title,tmp2.ChannelName, (Statistics.likes*1.0/nullif(Statistics.viewCount,0)) as Ratio FROM 
	(SELECT * FROM(
        SELECT * FROM(
            SELECT * FROM User WHERE userName like '%Marvel Entertainment%')
            tmp
        INNER JOIN Channel on tmp.userID = Channel.ownerID)  
    tmp1 
    INNER JOIN Video on tmp1.ChannelID = Video.ChannelID) tmp2
INNER JOIN Statistics ON Statistics.videoURL=tmp2.videoURL ORDER BY tmp2.title ASC