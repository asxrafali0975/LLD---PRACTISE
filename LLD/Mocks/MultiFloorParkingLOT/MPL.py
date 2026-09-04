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
    def __init__(self, number_of_floors) -> None:
        self.all_floor_data = {}
        self.number_of_floors = number_of_floors
        self.each_floor_locks = {}

        for i in range(number_of_floors):
            sm = int(input(f"Enter small vehicle parking available in floor {i} : "))
            md = int(input(f"Enter medium vehicle parking available in floor {i} : "))
            lr = int(input(f"Enter large vehicle parking available in floor {i} : "))

            self.all_floor_data[f"floor_{i}"] = {
                "small_area": {"Taken": {}, "NotTaken": {i for i in range(sm)}},
                "medium_area": {"Taken": {}, "NotTaken": {i for i in range(md)}},
                "large_area": {"Taken": {}, "NotTaken": {i for i in range(lr)}},
            }

            self.each_floor_locks[f"floor_{i}"]["small_area"] = Lock()
            self.each_floor_locks[f"floor_{i}"]["medium_area"] = Lock()
            self.each_floor_locks[f"floor_{i}"]["large_area"] = Lock()
        

        self.hashdict = {
                "small": "small_area",
                "medium": "medium_area",
                "large": "large_area",
            }

        # parking rates per hour
        self.parking_charges = {
            "small": 20,
            "medium": 50,
            "large": 100,
        }

    def Entry(self, vehicle: Vehicle):
        vehicle_type = vehicle.type()  # small , medium , large
        hash_dict_type = self.hashdict[vehicle_type] #"small_area" , "medium_area" , "large_area"
        particular_lock = self.each_floor_locks.get(hash_dict_type)
        with particular_lock:
        
            index = -1
            floor = None

            """
        Checking if vehicle already exist in Lot
            """

            for key in self.all_floor_data:
                parked_vehicle_data = self.all_floor_data[key][hash_dict_type]["Taken"].get(vehicle.vehicle_number)

                if parked_vehicle_data:
                    print("Error : Vehicle already exists in Parking LOT")
                    return

            """
        Checking for empty slots
            """

            for key in self.all_floor_data:
                value = self.all_floor_data[key][hash_dict_type]["NotTaken"]
                size =len(value)
                if size:
                    index = value.pop()
                    floor = key
                    break

            if index==-1 and floor==None:
                print("Parking LOT is FULL !! Sorry 😥")
                return 

            """
        now am getting 2 important things keyy ( which floor )
        and index ...
        so now my goal would be to insert data in that particular floor and index
            """

            data = {
            "entry_time": time.time(),
            "vehicle": vehicle,
            "floor" : floor,
            "index": index
            }

        

            self.all_floor_data[floor][hash_dict_type]["Taken"][vehicle.vehicle_number] = data

            print(f"vehicle parked successfully at floor {floor} and at label {index}")
        
                
    def Exit(self , vehicle: Vehicle):
        vehicle_type = vehicle.type() 
        hash_dict_type = self.hashdict[vehicle_type]
        particular_lock = self.each_floor_locks.get(hash_dict_type)
        with particular_lock:

            """
        first i need to check if  vehicle is parked or not then usko evict karna hai bas
            """

            parked_vehicle_data = None
            floor = None

            for key in self.all_floor_data:
                parked_vehicle_data = self.all_floor_data[key][hash_dict_type]["Taken"].get(vehicle.vehicle_number)
                if parked_vehicle_data:
                    floor = key

            if parked_vehicle_data is None:
                print("Error Vehicle not found in parking lot")
                return



            data = parked_vehicle_data
            parking_price =self.parking_charges[vehicle_type]
            current_time = time.time()
            total_hours =(current_time - data["entry_time"])/3600
            total_price = math.ceil(total_hours) * parking_price
            print(f"total cost is : {total_price}")

            """ 
        Now empty the taken
        
            """
            self.all_floor_data[floor][hash_dict_type]["NotTaken"].add(data["index"])
            del self.all_floor_data[floor][hash_dict_type]["Taken"][vehicle.vehicle_number]




        



if __name__ == "__main__":
    Pl = ParkingLot(1)
    b1 = Bike("9895")

    Pl.Entry(b1)
    Pl.Exit(b1)
    Pl.Exit(b1)
    
    pass
