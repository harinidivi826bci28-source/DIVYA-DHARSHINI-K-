#PROBLEM 9
m1=int(input("Mark 1:"))
m2=int(input("Mark 2:"))
m3=int(input("Mark 3:"))
m4=int(input("Mark 4:"))
total=m1+m2+m3+m4
average=(total/4)
print("total mark:",total)
print("average mark:",average)
if(average>=75):
    print("grade is distinction")
elif(average<75 and average>=60):
    print("grade is first class")
elif(average<60 and average>=50):
    print("grade is second class")
elif(average<50 and average>=40):
    print("grade is third class")
else:
     print("grade is fail")
