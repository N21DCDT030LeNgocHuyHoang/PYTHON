numDays= int(input("How many day's temperature?"))
total = 0
temp=[]
for i in range (1,numDays + 1):
    nextDay = int (input("Day"+str(i)+"'s high temp"))
    temp.append(nextDay)
    total = nextDay
avg = round(total/numDays,2)
print("\nAverage="+ str (avg))

above = 0
for i in temp:
    if i > avg:
        above +=1
print(str(above)+"day(s) above average")
