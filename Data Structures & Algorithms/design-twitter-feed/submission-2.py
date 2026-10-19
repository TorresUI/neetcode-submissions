class Twitter:

    def __init__(self):
        #map user ID to a list of tweet'IDs
        self.tweets = {}

        #map that takes in folwerID's and stores a list of who they are following
        self.following = {}

        #to get news feed take user id get list of follower id's then iterate through all their tweets from id -> tweets. combine all lists

        #keep track of tweet order
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        if userId not in self.following:
            self.following[userId] = set()
            self.following[userId].add(userId)
        
        #negative self time so that higher values are lower as minheap
        self.tweets[userId].append([-self.time, tweetId])
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        #We need to first get the follower list
        followerList = self.following[userId]
        totalFeed = []

        for i in followerList:
            tweetList = self.tweets[i]
            totalFeed += tweetList
        heapq.heapify(totalFeed)
        res = []
        for i in range(min(10, len(totalFeed))):
            time, tweet = heapq.heappop(totalFeed)
            res.append(tweet)
        
        return res
        


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followerList = self.following[followerId]
        if followeeId in followerList:
            followerList.remove(followeeId)

