#limit = 5 requests per minute

import time

class FixedWindowCounter:
    def __init__(self, max_request : int , time_frame : int) -> None:
        self.max_request = max_request
        self.time_frame = time_frame
        self.users = {}

    def hit_request(self, user_id : str)->str:
        current_time = time.time()

        if user_id  not in self.users:
            self.users[user_id] = {
                "current_window_start" : current_time ,
                "request_count" : 0
            }

        user_data = self.users[user_id]

        if current_time - user_data["current_window_start"] >= self.time_frame:
            user_data["current_window_start"] = current_time
            user_data["request_count"] = 0

        if user_data["request_count"]  >= self.max_request:
            return "rejected"

        user_data["request_count"]  = user_data["request_count"] +1
        return "worked performed"


        



if __name__=="__main__":

    max_request = 5
    time_frame = 1

    rate_limiter = FixedWindowCounter(max_request=max_request , time_frame=time_frame)

    




    pass

# print(time.time())