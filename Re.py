n = int(input("Enter the number of resistance: "))

All_Resistance = 0
Resistant_Value = []

for i in range(1,n+1,1):#start stop step
    x = int(input("Insert R {}".format(i) + " is "))
    Resistant_Value.append(1/x)

for i in Resistant_Value:
    All_Resistance = All_Resistance + i

print ("The Resistants are : ", Resistant_Value)
print ("Sums of Resistance is", 1/All_Resistance)
    
