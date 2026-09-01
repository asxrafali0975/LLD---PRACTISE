from abc import ABC , abstractmethod

class Notifications(ABC):
    @abstractmethod
    def send(self , user : str):
        pass


class EmailNotifications(Notifications):
    def send(self , user:str):
        print(f"send email notif to :  {user}")

class NotifDeco(Notifications):
    def __init__(self , object) -> None:
        self.object = object

    def send(self,user):
        self.object.send(user)


class PushDecorator(NotifDeco):
    def send(self, user: str):
        super().send(user) # pehle andar wala
        print(f"[PUSH] to {user}") # phir apna


class LoggingDecorator(NotifDeco):
    def send(self, user: str):
        super().send(user)
        print(f"[LOG] Sending to {user}")

if __name__=="__main__":

    n = EmailNotifications()
    n = PushDecorator(n)
    n = LoggingDecorator(n)

    n.send("loda lassun")

    pass