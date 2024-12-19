print("welcome to the tip calculator")
A = int(input("What was the total bill? $ "))
B = int(input("How much tip would you like to give? 10,12 or 15? "))
C = int(input("How many people to split the bill? "))
D = (B/100 * A + A)/C
print("Each person should pay : ",D)