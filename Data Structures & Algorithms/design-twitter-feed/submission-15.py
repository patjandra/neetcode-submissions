class Twitter:

    def __init__(self):
        self.followings = defaultdict(set) # user: [following]
        self.posts = defaultdict(list) # user: [posts]
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        feed.extend(self.posts[userId])
        for user in self.followings[userId]:
            feed.extend(self.posts[user])
        feed.sort(reverse=True)
        return [x[1] for x in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId in self.followings[followerId]:
            self.followings[followerId].remove(followeeId)
