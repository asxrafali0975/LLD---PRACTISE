from abc import ABC, abstractmethod
import time
from threading import Lock
import math


class Vehicle(ABC):
    @abstractmethod
    def type(self) -> str:
        pass


class Car(Vehicle):
    def __init__(self, vehicle_number: str):
        self.type_of_vehicle = "medium"
        self.tyres = 4
        self.vehicle_number = vehicle_number

    def type(self) -> str:
        return self.type_of_vehicle


class Bike(Vehicle):
    def __init__(self, vehicle_number: str):
        self.type_of_vehicle = "small"
        self.tyres = 2
        self.vehicle_number = vehicle_number

    def type(self) -> str:
        return self.type_of_vehicle


class Truck(Vehicle):
    def __init__(self, vehicle_number: str):
        self.type_of_vehicle = "large"
        self.tyres = 4
        self.vehicle_number = vehicle_number

    def type(self) -> str:
        return self.type_of_vehicle


class ParkingLot:

    def __init__(self, max_small: int, max_medium: int, max_large: int) -> None:
        self.small_area = {"Taken": {}, "NotTaken": {i for i in range(max_small)}}
        self.large_area = {"Taken": {}, "NotTaken": {i for i in range(max_large)}}
        self.medium_area = {"Taken": {}, "NotTaken": {i for i in range(max_medium)}}
        self._lock = Lock()

    def set_price(self, small_perhr: int, medium_perhr: int, large_perhr: int):
        self.parking_price = {
            "small": small_perhr,
            "medium": medium_perhr,
            "large": large_perhr,
        }

    def Entry(self, vehicle: Vehicle):
        with self._lock:
            type_of_vehicle: str = vehicle.type()

            hashdict = {
                "small": self.small_area,
                "medium": self.medium_area,
                "large": self.large_area,
            }

            # now we need to take out a area for this vehicle
            which_area_occupy = hashdict[type_of_vehicle]

            if len(which_area_occupy["NotTaken"]) == 0:
                print("ALERT : Parking Lot is Full !!")
                return

            if which_area_occupy["Taken"].get(vehicle.vehicle_number):
                print("ERROR :  Vehicle already in parking lot !!")
                return

            area_not_taken = which_area_occupy["NotTaken"].pop()
            data = {
                "entry_time": time.time(),
                "vehicle": vehicle,
                "index": area_not_taken,
            }

            which_area_occupy["Taken"][vehicle.vehicle_number] = data

    def check_out(self, vehicle: Vehicle):
        with self._lock:

            type_of_vehicle: str = vehicle.type()

            hashdict = {
                "small": self.small_area,
                "medium": self.medium_area,
                "large": self.large_area,
            }
            which_area_occupy = hashdict[type_of_vehicle]

            # if parking lot is already empty we cant evict items...
            if len(which_area_occupy["Taken"]) == 0:
                print("parking lot is empty ")
                return

            parking_price = self.parking_price[type_of_vehicle]

            if not which_area_occupy["Taken"].get(vehicle.vehicle_number):
                print("ERROR :  Vehicle is not present in parking lot !!")
                return

            parked_data = which_area_occupy["Taken"][vehicle.vehicle_number]
            parked_time = parked_data["entry_time"]
            current_time = time.time()
            total_seconds = current_time - parked_time
            total_hours = total_seconds / 3600

            total_price = math.ceil(total_hours) * parking_price
            print(f"total cost is : {total_price}")

            # now empty that spot..
            index = parked_data["index"]
            which_area_occupy["NotTaken"].add(index)
            del which_area_occupy["Taken"][vehicle.vehicle_number]


if __name__ == "__main__":

    Ash_Parkings = ParkingLot(10, 5, 2)
    Ash_Parkings.set_price(20, 50, 100)
    car1 = Car("9895")
    bike1 = Bike("9476")
    pass
