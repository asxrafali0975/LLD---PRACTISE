class Node:
    def __init__(self , before : Node | None = None , after : Node | None = None , value : str = "None" , key : str = "None") -> None:
        self.before = before
        self.after = after
        self.value = value
        self.key = key


class LRU:
    def __init__(self , size:int) -> None:
        self.hash = {}
        self.front = None
        self.size = size
        self.back = None

    def get(self , key : str):
        #first check if key is present in the hash or not

        #if present
        if self.hash.get(key):
            print(f"value is : {self.hash[key].value}")

            node = self.hash[key]

            if  node!=self.front:

                if node ==self.back:
                    second_last_node = node.before
                    second_last_node.after = None
                    node.before = None
                    node.after = self.front
                    self.front.before = node
                    self.back = second_last_node
                    self.front = node
                    return 

                #this will mean that its present in between
                before_node = node.before
                after_node = node.after
                before_node.after = after_node
                after_node.before = before_node

                node.after = self.front
                self.front.before = node
                self.front = node

                



        #not present
        #fetch from db
        else:
            n = int(input("Enter a number : "))
            #example fetched this node from db
            print(f"value is : {n} ")
            node = Node(value=n , key=key) 
            if self.front is None:
                self.front = node
                self.back = node
                
              
            else:
                node.after = self.front
                self.front.before = node
                self.front = node

            self.hash[key] = node

            if len(self.hash) > self.size:
                #only if one single node is exsisting
                if self.front==self.back:
                    del self.hash[self.front.key] #eror
                    self.front=None
                    self.back= None


                else:
                    end_node = self.back
                    del self.hash[end_node.key]
                    second_last_node = end_node.before
                    second_last_node.after = None
                    end_node.before = None
                    self.back = second_last_node

                

       

