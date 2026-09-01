from abc import ABC , abstractmethod
import time
from threading import Lock
from collections import deque


type_of_users : dict[str , int] = {
    "premium" : 100,
    "normal" : 50
}

redis_log_store = {}

user_lock_store = {}

TIME_LIMIT = 60 # seconds me

class User:
    def __init__(self, user_id : str, tier : str):
        self.user_id = user_id
        self.tier = tier
        self.time_limit = 60 #seconds



class RateLimiter(ABC): #interface

    @abstractmethod
    def hit_request(self,user : User):
        pass



class SlidingWindowLog(RateLimiter):
       

    def hit_request(self, user : User ):
        rate  = type_of_users[ user.tier ]
        current_time = time.time()
        user_log : deque = redis_log_store.setdefault(user.user_id, deque())
        user_lock = user_lock_store.setdefault(user.user_id, Lock())

        with user_lock:

            while user_log and current_time - user_log[0] >= user.time_limit:
                user_log.popleft()

            if len(user_log) >=rate:
                return "rejected with 429 , too many request "

            user_log.append(current_time)

            redis_log_store[user.user_id] = user_log

        user_lock_store[user.user_id] = user_lock

        return "accepted  , 200 OK"


class NewAlgorithm(RateLimiter):
    def hit_request(self, user : User):
        print(user)


class RateLimiterService:
    def __init__(self , which_class : RateLimiter) -> None:
        self.rate_limiter_object = which_class
    def hit_request(self , user : User):
        self.rate_limiter_object.hit_request(user)

    



        

if __name__=="__main__":
    ash  = User("ash123" , "premium")
    aqsa  = User("aqsa143" , "normal")

    # sliding_window_algo = SlidingWindowLog()
    # sliding_window_algo.hit_request(ash)
    # sliding_window_algo.hit_request(aqsa)

    rlo = RateLimiterService(SlidingWindowLog())
    rlo.hit_request(ash)
    pass



        