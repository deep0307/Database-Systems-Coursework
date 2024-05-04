-- SQLite
-- First I performed the SELECT operation to obtain those channels whose creation data was 2023-01-01 using the LIKE command(stored it in tmp1).
-- Next I performed INNER JOIN on the Subscription Table and the table obtained from above on the condition that Subscription.channelID=tmp1.channelID
-- while performing INNER JOIN as mentioned above, I performed GROUP BY operation on the column: channelID.
-- The reason for doing GROUP BY was because I wanted to use the count() function to count the number of Paid Subscribers. If I do not perform the GROUP BY operation, then the output of the table is just a single value and count of paid subscibers across all channels which I did not need.
-- In the count function I used a case which is a condition in which if the subscriptionType column is "Paid" then it returns 1 otherwise it returns 0.
-- The above table was stored in tmp
-- Now in order to display the information according to Q3, I finally performed INNER JOIN on the User table and tmp table on the condition that User.userID=tmp.ownerID.
-- Before displaying the information there was 1 final condition that the number of Paid subscribers must be greater than 100. This was added in the where condition and finally athe information was displayed as per requirement.
 
SELECT User.userName,User.userEmail,tmp.ChannelName,tmp.subscriptionCount from User 
	INNER JOIN 
		(SELECT *,count(case when Subscription.subscriptionType = 'Paid' then 1 else null end) as PaidCount FROM Subscription 
			INNER JOIN 
				(SELECT * from Channel where creationDateTime like '%2023-01-01%') 
			tmp1 ON Subscription.channelID=tmp1.channelID GROUP BY Subscription.channelID) 
	tmp ON User.userID=tmp.ownerID where tmp.PaidCount>100
