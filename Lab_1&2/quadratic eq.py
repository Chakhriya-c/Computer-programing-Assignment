import math

# [-b +- sqrt(b**2 - 4ac)] / 2(a)

a = int(input("Defien the a: "))
b = int(input("Defien the b: "))
c = int(input("Defien the c: "))

eq = math.pow(b,2) - (4 * a * c)

sq_eq = math.sqrt(abs(eq))

if eq > 0 :
    print ((-b+sq_eq) / (2*a))
    print ((-b-sq_eq) / (2*a))

elif eq == 0 :
            print (-b/(2*a))

elif eq < 0 :
            print ((-b+sq_eq)/(2*a) ,"+i", sq_eq)
            print ((-b+sq_eq)/(2*a) ,"-i", sq_eq)

else:
    print ("Hmm, What is this?")
