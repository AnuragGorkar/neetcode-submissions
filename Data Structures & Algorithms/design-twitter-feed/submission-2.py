class TwitterUser: 
    def __init__(self, id): 
        self.id = id
        self.tweet_queue = deque(maxlen=10)
        self.followee_list = set()
        self.followee_list.add(id)
    
    def addFollowee(self, userId): 
        self.followee_list.add(userId)
    
    def removeFollowee(self, userId):
        if userId != self.id: 
            self.followee_list.discard(userId)
    
    def getFollowees(self): 
        return self.followee_list

    def postTweet(self, tweet):
        self.tweet_queue.append(tweet)
    
    def getTweets(self): 
        return list(self.tweet_queue)
    
    def getNewsFeed(self, followee_list):
        all_feed = []
        for followee in followee_list:
            all_feed.extend(followee.getTweets())
        heapq.heapify(all_feed)
        feed = []
        while len(all_feed) and len(feed)<10: 
            post = heapq.heappop(all_feed)
            feed.append(post[1])
        return feed

class Twitter:
    tweet_count = 0
    def __init__(self):
        self.users_map = dict()
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        user = self.users_map.setdefault(userId, TwitterUser(userId))
        Twitter.tweet_count += 1
        user.postTweet((-1*Twitter.tweet_count, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        user = self.users_map.setdefault(userId, TwitterUser(userId))
        followee_list = [self.users_map[x] for x in user.getFollowees()]
        return user.getNewsFeed(followee_list)
        
    def follow(self, followerId: int, followeeId: int) -> None:
        user = self.users_map.setdefault(followerId, TwitterUser(followerId))
        user.addFollowee(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        user = self.users_map.setdefault(followerId, TwitterUser(followerId))
        user.removeFollowee(followeeId)
        
