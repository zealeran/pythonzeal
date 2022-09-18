print("******************* BOOK MY SHOW****************")
theater_location={"1.vetri":"chrompet","2.ganesh":"Anakaputhur","3.pvr":"meenambakkam"}
print(theater_location)
choice=str(input("please select you theater:"))

print("1.ps1""\t2.sinam","\t3.vtk")
movies=str(input("please select your movie:")).lower().strip()
select=["1. 6.30 A.M","2. 2.00 P.M","3. 9.00 P.M"]
print(select)
timing=int(input("please select your timing:"))

seat=250
member=int(input("please enter how many tickets you want:"))
balance_seat=seat-member
if member>250:
    print("The thicket is unavailabel ")
elif member<=250:
    print(f" ticket is availableis and the balance ticket is {balance_seat}")
    print(f"your have booked {member} tickets")
if movies=="ps1":
    def ps1(timing,member):
        if timing==1:
            print("Your booking is available")
        elif timing==2:
            print("Your booking is in waiting")
        elif timing==3:
            print("Your booking is available")
        else:
            print("please select in  the given timing.")
        amount=member*120
        print(f"ypur total amount is{amount}")
    ps1(timing,member)
elif movies=="sinam":
    def sinam(timing,member):
        if timing==1:
            print("Your booking is available")
        elif timing==2:
            print("Your booking is in waiting")
        elif timing==3:
            print("Your booking is available")
        else:
            print("please select in  the given timing.")
        amount=member*120
        print(f"ypur total amount is{amount}")
    sinam(timing,member)
elif movies=="vtk":
    def vtk(timing,member):
        if timing==1:
            print("Your booking is available")
        elif timing==2:
            print("Your booking is in waiting")
        elif timing==3:
            print("Your booking is available")
        else:
            print("please select in  the given timing.")
        amount=member*120
        print(f"ypur total amount is{amount}")
    vtk(timing,member)

