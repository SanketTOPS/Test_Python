class student:
    stid=12
    stnm='Sanket'

    def __getdata(self): #private
        print("This is getdata.")
    
    def myfunc(self): #public
        self.__getdata()


st=student()
print(st.stid)
print(st.stnm)
st.myfunc()
