n = int(input("Enter the number of resistance: "))

all_Resistance = 0
resistant_value = []

for i in range(1,n+1,1):#start stop step
    x = int(input("Insert R {}".format(i) + " is "))
    resistant_value.append(1/x)

for i in resistant_value:
    all_resistance = all_resistance + i

print ("The Resistants are : ", resistant_value)
print ("Sums of Resistance is", 1/all_resistance)
    
