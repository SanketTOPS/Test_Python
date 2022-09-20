class student:
    stid=12
    stnm='Sanket'

    def getdata(self):
        print("This is getdata.")


# Calling a classs
st=student()
print(st.stid)
print(st.stnm)
st.getdata()