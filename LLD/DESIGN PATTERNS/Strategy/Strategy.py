from abc import ABC , abstractmethod

class PaymentStrategies(ABC):
    def pay(self):
        pass

class UPI(PaymentStrategies):
    def pay(self):
        print("payed using UPI")


class PayTM(PaymentStrategies):
    def pay(self):
        print("payed using Paytm")



# class Application:
#     def __init__(self , app : str) -> None:
#         print(f"{app} : application")
#     def make_payment(self , PayService : PaymentStrategies):
#         PayService.pay()

class Application:
    def __init__(self ,PayService : PaymentStrategies ) -> None:
        self.object = PayService
    def make_payment(self):
        self.object.pay()





if __name__=="__main__":
    payment = Application(PayTM())
    payment.make_payment()

    payment= Application(UPI())
    payment.make_payment()


    pass

    



    
