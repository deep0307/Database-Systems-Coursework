In this diagram, the Users Entity is a supertype having a total disjoint constraint and has 2 subtypes- video creator and video consumer.

Video creator creates channels where video creators can upload videos to. Video consumer subscribes to these channel (can subscribe upto N channels).

Each channel has the no of subscribers and the details of when the channel was created.

Videos have a URL which is unique for each video and thus is the primary key. It also has a title, category, thumbnails, description, etc. as its attributes. 

Videos is another supertype having total disjoint constraint and its 2 subtypes are - informational videos and education videos.

Informational videos are based on keywords whereas entertainment videos are based on tags.

Each videa has statistics like no of likes, disklikes, shares, etc.

Each video can have comments which stores the text, likes, sentiment and the details of the comment.

The video creators earn revenue through sponsors who sponsor the videos. The sponsor entity has the name, phone, address and amount sponsored.
 