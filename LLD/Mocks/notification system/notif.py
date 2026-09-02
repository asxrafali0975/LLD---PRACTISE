from abc import ABC, abstractmethod
import random



class INotificationChannel(ABC):
    @abstractmethod
    def send(self,  data: str):
        pass


class EmailNotification(INotificationChannel):
    def __init__(self , email : str) -> None:
        self.email = email
    def send(self, data: str):
        print(f"sended data : {data} to email id : {self.email} ")


class SMSNotification(INotificationChannel):
    def __init__(self , phone_number : str) -> None:
        self.phone_number = phone_number
    def send(self, data: str):
        print(f"sended data : {data} to SMS Number: {self.phone_number} ")


class INotificationType(ABC):
    @abstractmethod
    def create_message(self, data: str):
        pass


class OrderConfirmation(INotificationType):
    def create_message(self, data: str):
        return f"""
                THIS IS ORDER CONFIRMATION NOTIFICATION FROM BIG BAZAR
                {data}
                """

    # example -> "Your odered of {product} with product id : {random.randint(1000 , 9999)} has been confirmed "


class PasswordReset(INotificationType):
    def create_message(self, data: str):
        return f"""
        THIS IS PASSWORD RESET CONFIRMATION MAIL
        {data}

PLEASE DO NOT REPLY TO THIS MAIL
        """  # example -> "Your password is successfully reseted"


class NotificationEngine:
    def notify(self, channel_array : list[INotificationChannel], notification_type :  INotificationType,  data : str):
        value = notification_type.create_message(data)

        for channel in channel_array:
            try:
                channel.send(value)
            except Exception as e:
                print(f"failed to send data to : {channel} , error : {str(e)}")
        


if __name__ == "__main__":

    NE = NotificationEngine()
    NE.notify(
        [EmailNotification("ashrafalistudy@gmail.com") , SMSNotification("+91-9935630224")],
        OrderConfirmation(),
        
        "order id : 123",
    )

    pass
