
import time
from collections import deque

class SlidingWindowLogs:
    def __init__(self , max_requests : int , time_frame: int) -> None:
        self.max_requests = max_requests
        self.time_frame = time_frame
        self.logs = deque()

    def hit_request(self):
        current_time = time.time()
        size = len(self.logs)

        while size and  current_time - self.logs[0] >= self.time_frame:
            self.logs.popleft()

        if len(self.logs)>=self.max_requests:
            return "rejected"

        self.logs.append(current_time)
        return "Accepted"

if __name__=="__main__":
    rate_limiter = SlidingWindowLogs(
        max_requests=5,
        time_frame=60
    )
    for i in range(7):
        result = rate_limiter.hit_request()
        print(f"{i + 1}: {result}")

        