class grandfather:
    gold=0
    house=0

    def g_getdata(self):
        self.house=input("Enter House details:")
        self.gold=input("Enter Gold Details:")

class father(grandfather):
    car=0
    bal=0

    def f_getdata(self):
        self.car=input("Enter car details:")
        self.bal=input("Enter balance details:")

class son(father):
    def alldata(self):
        print("House:",self.house)
        print("Gold:",self.gold)
        print("Car:",self.car)
        print("Balance:",self.bal)

sn=son()
sn.g_getdata()
sn.f_getdata()
sn.alldata()
