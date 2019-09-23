import praw

class subreddit(object):
    reddit = praw.Reddit(client_id='4IYYAb5DPvSHvw',
                         client_secret='6q1QJV-AoVefGKgMElFShEJxnhg',
                         user_agent='test the wrapper')
                         # username='my username',
                         # password='my password')
    #default sub to news
    def __init__(self,sub='news'):
        self.name=sub
    #method for hot sub, default = 5 titles
    def hotSub(self,lim=5):
        #for submission in self.reddit.subreddit(self.name).hot(limit=lim):
         #   print(submission.title)
        return list(self.reddit.subreddit(self.name).hot(limit=lim))
    #method for top sub, default = 5 titles
    def topSub(self,lim=5):
        for submission in self.reddit.subreddit(self.name).top(limit=lim):
            print(submission.title)
    #method for new sub, default = 5 titles
    def newSub(self,lim=5):
        for submission in self.reddit.subreddit(self.name).new(limit=lim):
            print(submission.title)
