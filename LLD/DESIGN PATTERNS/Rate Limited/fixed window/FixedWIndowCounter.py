#limit = 5 requests per minute

import time

class FixedWindowCounter:
    def __init__(self, max_request : int , time_frame : int) -> None:
        self.max_request = max_request
        self.time_frame = time_frame
        self.current_window_start = time.time()
        self.request_count = 0

    def hit_request(self)->str:
        current_time = time.time()

        if current_time - self.current_window_start >= self.time_frame:
            self.current_window_start = current_time
            self.request_count = 0

        if self.request_count >= self.max_request:
            return "rejected"


        self.request_count+=1
        return "worked performed"


        



if __name__=="__main__":

    max_request = 5
    time_frame = 1

    rate_limiter = FixedWindowCounter(max_request=max_request , time_frame=time_frame)

    for i in range(1,50):
        ans = rate_limiter.hit_request()
        print(f"{i} : {ans}")
        time.sleep(0.1)




    pass

# print(time.time())