class laptop():
    chargertype="C-Type"

    def __init__(self):
        self.Brand=""
        self.Price=35

    def setPrice(self,Price):
        self.Price=Price

    def getprice(self):
        print(self.Price)
    @classmethod
    def chargetype(cls):
        cls.chargertype="B-Type"
        print("chargertype:",cls.chargertype)
        print("chargertype is changed to B")
    @staticmethod
    def info():
        print("this is laptop class")


hp=laptop()
hp.setPrice(20000)
hp.getprice()


laptop.chargetype()

hp.info()
        
