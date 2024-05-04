-- SQLite
-- In this query I first obtain the sponsor who has sponsored the most. This is done by using group by on sponsorID and performed Sum operation on sponsorAmount column and stored it as Amount. 
-- Then I ordered the newly obtained Amount column in descending order (using ORDER BY Amount desc).
-- Then I performed SELECT operation to get only the first row as that sponsor is the highest sponsor (used 'LIMIT 1') 
-- Next I performed INNER JOIN on the SponsorList table and the tmp table obtained through query mentioned above on the condition that SponsorList.sponsorID = tmp.sponsorID.
-- Finally I performed SELECT opertion to display the details of the sponsor as per the requirements of Q1.


SELECT SponsorList.sponsorName,SponsorList.sponsorPhone,tmp.Amount from SponsorList 
	INNER JOIN 
		(SELECT * FROM (SELECT sponsorID,sum(sponsorAmount) as Amount from SponsoringVideo GROUP BY sponsorID ORDER BY Amount DESC) LIMIT 1)
	tmp ON  SponsorList.sponsorID=tmp.sponsorID

 