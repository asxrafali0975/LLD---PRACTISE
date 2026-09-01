from abc import ABC, abstractmethod


class Notifications(ABC):

    @abstractmethod
    def notify(self, name: str, number: int, email: str, message: str):
        pass


class WhatsappNotifications(Notifications):
    def notify(self, name: str, number: int, email: str, message: str):
        print(f"sent {message} to address : {number}")


class EmailNotifications(Notifications):
    def notify(self, name: str, number: int, email: str, message: str):
        print(f"sent {message} to address : {email}")


class Subscriber:
    def __init__(
        self, name: str, number: int, email: str, notif: Notifications
    ) -> None:
        self.name = name
        self.number = number
        self.email = email
        self.notifier = notif

    def notify_to_users(self, data: str):
        self.notifier.notify(self.name, self.number, self.email, data)


class Publisher:
    def __init__(self, current_stock_price: int, stock_name: str) -> None:
        self.subscribers_list: list[Subscriber] = []
        self.current_stock_price = current_stock_price
        self.stock_name = stock_name

    def update(self, data: str):
        for subs in self.subscribers_list:
            try:
                subs.notify_to_users(data)
            except Exception as e:
                print(f"failed to notify {subs.name} ")

    def stock_price_increase(self, value: int):
        self.current_stock_price = self.current_stock_price + value

        # update function
        self.update(f"stock prices have beem increased by :{value} ")

    def stock_price_decrease(self, value: int):
        self.current_stock_price = self.current_stock_price - value
        self.update(f"stock prices have beem decreased by :{value} ")

    def get_stock_price(self):
        print(self.current_stock_price)

    def add_subscriber(self, sub: Subscriber):
        self.subscribers_list.append(sub)


if __name__ == "__main__":

    Wipro = Publisher(400, "Wipro")
    Ashraf = Subscriber(
        "ashraf", 9935630224, "ashrafalistudy@gmail.com", EmailNotifications()
    )

    aqsa = Subscriber("aqsa", 8429781054, "aqsa@gmail.com", WhatsappNotifications())

    Wipro.add_subscriber(Ashraf)
    Wipro.add_subscriber(aqsa)
    Wipro.stock_price_increase(100)

    pass
