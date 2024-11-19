class mobile():
    chargertype="C-type"

    def __init__(self,Brand,Price):
        self.Brand=Brand
        self.Price=Price

    def display(self):
        print("Brand:",self.Brand)
        print("Price:",self.Price)
        print("Chargertype:",self.chargertype)

mobile.chargertype="B-type"


Samsung=mobile("Samsung","50,000")
Samsung.display()

Google=mobile("pixel","1,00,000")
Google.display()
        
