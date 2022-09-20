class nirav:
    nid=0
    nbranch=''

    def n_getdata(self):
        self.nid=input("Enter Nirav's ID:")
        self.nbranch=input("Enter Nirav's Branch:")

class mitesh:
    mid=0
    mbranch=''

    def m_getdata(self):
        self.mid=input("Enter Mitesh's ID:")
        self.mbranch=input("Enter Mitesh's Branch:")

class gtu(nirav,mitesh):
    def alldata(self):
        print("Nirav ID:",self.nid)
        print("Nirav Branch:",self.nbranch)
        print("Mitesh ID:",self.mid)
        print("Mitesh Branch:",self.mbranch)

gt=gtu()
gt.n_getdata()
gt.m_getdata()
gt.alldata()


