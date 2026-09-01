from abc import ABC , abstractmethod 

class Subscribers(ABC):


    def __init__(self , name : str) -> None:
        self.name = name

    @abstractmethod
    def notify(self,video_title:str , publisher : str):
        pass

class YoutubeNotify(Subscribers):
    def notify(self,video_title:str,publisher : str):
        print(f"{self.name} , {publisher} has uploaded new video of title {video_title}")
        pass

        

class Publisher : 

    def __init__(self,channel_name : str) -> None:
        self.channel_name = channel_name
        self.subscribers : list[Subscribers] = []

    def add_subscriber(self,sub : Subscribers):
        self.subscribers.append(sub)

    def published_video(self,video_title:str):
        for subs in self.subscribers:
            try:
                subs.notify(video_title , self.channel_name)
            except Exception as e:
                print(f"Failed to notify {subs.name}: {e}")




           


if __name__=="__main__":
    Ashraf = Publisher("ashraf-ali")
    Ashraf.add_subscriber(YoutubeNotify("vaibhavi"))
    Ashraf.add_subscriber(YoutubeNotify("aqsa"))

    Ashraf.published_video("how does python works?")

    pass


    
        