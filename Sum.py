
number = int(input("\nThis program will calculate the sum of all the numbers between 0 and :"))

sum = 0
i = number

if number <= 0:
    print("This number is not positive")

else :
    while i > 0:
        sum = sum + i
        i = i - 1
    
    print("\nThe sum between 0 and " +str(number)+ " is " +str(sum))

