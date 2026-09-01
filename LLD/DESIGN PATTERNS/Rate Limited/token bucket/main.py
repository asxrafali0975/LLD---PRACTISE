
import time 


class TokenBucket:
    def __init__(self, max_request : int, time_frame : int):
        self.tokens = max_request
        self.time_frame = time_frame
        self.max_request = max_request
        self.last_update_time = time.time()

    def hit_request(self):
        current_time = time.time()

        time_elapsed = current_time - self.last_update_time
        rate = self.max_request / self.time_frame
        self.tokens =   min(self.max_request , self.tokens + int(rate*time_elapsed))
        self.last_update_time = current_time

        if self.tokens <=0:
            return "rejected"


        self.tokens -=1
        return "accepted"

        
        