class dad():
    def phone(self):
        print("dad's phone")


class laptop():
    def laptopcharger(self):
        print("charger")

class son1(dad,laptop):
    pass


class son2(dad):
    pass

class son3(dad):
    pass


s1=son1()
s1.laptopcharger()

