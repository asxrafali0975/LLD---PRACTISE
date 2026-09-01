from abc import ABC , abstractmethod

class abstract_class(ABC):
    def request(self):
        pass

class client:
    def request(self,abc_class : abstract_class):
        abc_class.request()
        

class adapter(abstract_class):
    def request(self):
        lib  = Library()
        lib.new_function()
        

class Library:
    def library_function(self):
        print("i do the old work")

    def new_function(self):
        print("i do the new work")

if __name__=="__main__":

    c = client()
    c.request(adapter())

    pass