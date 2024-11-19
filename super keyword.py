class a():
    def __init__(self):
        super().__init__()
        print("A")


    def display(self):
        print("your in a class")


class b():
    def __init__(self):
        super().__init__()
        print("B")

        
    def display(self):
        print("your in b class")


class c(a,b):
    def __init__(self):
        super().__init__()
        print("C")

        
    def display(self):
        print("your in c class")


obj=c()
    
