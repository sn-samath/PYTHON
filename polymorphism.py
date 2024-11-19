class animals():
    def sound(self):
        print("Animal makes sound")


class dog(animals):
    def sound(self):
        print("dog brakes")

class bird (animals):
    def sound(self):
        print("birds sing")


obj=bird()
obj.sound()
