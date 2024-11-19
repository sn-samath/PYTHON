class company():
    def __init__(self):
        self.__companyName="Google"
class b(company):
    pass
c1=company()
c1.__init()
print(c1.__companyName)
