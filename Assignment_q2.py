#Program for doing sum of range using ForLoop

startNumber = int(input("Enter Starting Number : "))
endNumber = int(input("Enter Last Number : "))
sumOfRange = 0

for i in range(startNumber,endNumber+1):
    sumOfRange = sumOfRange + i

print("The sum of number from ", startNumber, "to", endNumber, "is :",sumOfRange)
