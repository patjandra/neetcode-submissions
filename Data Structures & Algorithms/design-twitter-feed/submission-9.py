class Twitter:

    def __init__(self):
        self.following = defaultdict(set) # userId : [followeeIds, ...]
        self.posts = defaultdict(list) # userId : [(time, tweetId), ...]
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # generate new feed each time to account for follows/unfollows
        feed = []
        #append users posts to feed
        for post in self.posts[userId]:
            feed.append(post)
        #append following posts to feed
        for following in self.following[userId]:
            for post in self.posts[following]:
                feed.append(post)
        #sort posts by recency and cut to 10
        feed.sort(reverse=True)
        feed = feed[:10]
        #return only tweetIds
        return [post[1] for post in feed]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].discard(followeeId)