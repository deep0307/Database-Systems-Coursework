-- SQLite
-- First I performed SELECT operation on the InfoVideo table to obtain all the keywords assigned to each informational video(stored it in tmp).
-- After that I performed INNER JOIN on the Comment table and the table obtained from above on the condition that Comment.videoURL = tmp.videoURL.
-- Then I performed GROUP BY operation on the keywords column as I wanted to take the average sentiment score for each keyword.
-- Then I finally performed avg() function on the Comment.sentiment column (this column is a sentiment score from a range of 0-100) and stored it in the AverageSentimentScore column.
-- According the the requirements of Q4, the average sentiment score of each keyword must be displayed in the descending order, so I used ORDER BY function on the AverageSentimentScore column.
-- Finally I displayed all the information as per requirements.

SELECT tmp.keywords,avg(Comment.sentiment) as AverageSentimentScore FROM Comment 
	INNER JOIN 
		(SELECT * from InfoVideo) 
	tmp WHERE Comment.videoURL=tmp.videoURL GROUP BY tmp.keywords ORDER BY AverageSentimentScore DESC