class laptop:
    def __init__(self):
        ram=" "
        processor=" "

    def display(self):
        print("ram",self.ram)
        print("processor",self.processor)


hp=laptop()
dell=laptop()

hp.ram="8GB"
hp.processor="i7"

dell.ram="16GB"
dell.processor="i9"

hp.display()


dell.display()
        
