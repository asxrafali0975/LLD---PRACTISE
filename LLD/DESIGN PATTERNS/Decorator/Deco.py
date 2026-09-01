from abc import ABC , abstractmethod

class Notifications(ABC):
    @abstractmethod
    def send(self , user : str):
        pass


class EmailNotifications(Notifications):
    def send(self , user:str):
        print(f"send email notif to :  {user}")

class YoutubeNotifications(Notifications):
    def send(self , user:str):
        print(f"send youtube notif to :  {user}")


class PushDecorator(Notifications):
    def __init__(self , object : Notifications) -> None:
        self.object = object

    def send(self, user: str):
        self.object.send(user)
        print(f"send push notif to :  {user}")

if __name__=="__main__":
    email = EmailNotifications()
    email.send("ashraf")


    yt = YoutubeNotifications()
    yt.send("aqsa")

    push = PushDecorator(EmailNotifications())
    push.send("kanika")



