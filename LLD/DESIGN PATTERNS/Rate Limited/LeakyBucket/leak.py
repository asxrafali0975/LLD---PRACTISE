import time
import threading
from collections import deque

class LeakyBucket:
    def __init__(self, bucket_capacity: int, leak_rate: float):
        self.bucket_capacity= bucket_capacity
        self.leak_rate = leak_rate
        self.queue = deque()
        self.lock = threading.Lock()

        self.worker = threading.Thread(
            target=self.leak,
            daemon=True
        )

        self.worker.start()


    def leak(self):
        #in every 2 seconds ...if queue is empty do nothing , else if requests are present
        #process it 
        while True:
            time.sleep(self.leak_rate)

            with self.lock:
                if self.queue:
                    request = self.queue.popleft()
                    print("work performed\n")


    def hit_request(self):
        with self.lock:
            current_time = time.time()

            if len(self.queue) >= self.bucket_capacity:
                print("rejected\n")
            self.queue.append(current_time)
            

        
        

        



if __name__=="__main__":

    rate_limiter  = LeakyBucket(3 , 1)

    while True:
        x = int(input("enter a number : "))
        if x==1:
            rate_limiter.hit_request()
        else:
            break



    pass