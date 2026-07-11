class Twitter:

    def __init__(self):
        # tweet storage
        # tweet relationship to user
        # tweet order handling on followers using heap on top 10
        # {user123: deque(tweetid, time)}
        self.user_tweet = defaultdict(deque)

        # user storage
        # user relationship to user
        # {user123: set(user123, user456, user1, user4)}
        self.user_user = defaultdict(set)


        # time for judging most recent push
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweet[userId].appendleft((self.time, tweetId))
        self.time += 1

        if len(self.user_tweet[userId]) > 10:
            self.user_tweet[userId].pop()

    def getting_top_10(self, lst) -> List[int]:
        if not lst: return []
        # [[(time, tweetid)], ...]
        candidate_idx = [0] * len(lst)
        ret = []

        for _ in range(10):
            max_ele = (-1, -1)
            max_ele_idx = -1
            for idx in range(len(lst)):
                if candidate_idx[idx] == -1 or not lst[idx]:
                    continue
                curr_ele = lst[idx][candidate_idx[idx]]
                if max_ele[0] < curr_ele[0]:
                    max_ele_idx = idx
                    max_ele = curr_ele
            
            if max_ele_idx != -1:
                # update candidate_idx
                candidate_idx[max_ele_idx] += 1
                if candidate_idx[max_ele_idx] == len(lst[max_ele_idx]):
                    candidate_idx[max_ele_idx] = -1

                ret.append(max_ele[1])
        return ret

    def getNewsFeed(self, userId: int) -> List[int]:
        all_post = [self.user_tweet[userId]]
        for user_followed in self.user_user[userId]:
            all_post.append(self.user_tweet[user_followed])

        # getting top 10
        return self.getting_top_10(all_post)

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        if followeeId not in self.user_user[followerId]:
            self.user_user[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or (not followeeId in self.user_user[followerId]):
            return
        self.user_user[followerId].discard(followeeId)
        
