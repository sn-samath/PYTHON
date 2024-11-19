class calculator:
    def __init__(self,value1,value2):
        self.a=value1
        self.b=value2
        
    def add(self):
        print("add:",self.a+self.b)

    def sub(self):
        print("sub:",self.a-self.b)

    def div(self):
        print("div:",self.a/self.b)

    def mul(self):
        print("multi:",self.a*self.b)

plus=calculator(10,20)

plus.add()
plus.sub()
plus.div()
plus.mul()
        
