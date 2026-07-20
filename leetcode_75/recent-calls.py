# 933. Number of Recent Calls

# You have a RecentCounter class which counts the number of recent requests within a certain time frame.

# Implement the RecentCounter class:

# RecentCounter() Initializes the counter with zero recent requests.
# int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, 
# and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, 
# return the number of requests that have happened in the inclusive range [t - 3000, t].

from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.counter = deque()
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.counter.append(t)

        while self.counter:
            val = self.counter[0]
            if val < t - 3000:
                self.counter.popleft()
            else:
                break

        return len(self.counter)        


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3001))
print(obj.ping(3002))
