# Program to take input percentage 
# prints out corresponding the grade

p = float(input("Please enter percentage mark: "))

p = round(p)
print("percentage = ",p)

if p < 0 or p > 100:
    print("Not Valid")

elif p < 40:
    print("=> FAIL")

elif 40 <= p <= 49:
    print("=> PASS")

elif  50 <= p <= 59:
    print("=> Merit 2")

elif 60 <= p <= 69:
    print("=> Mert 1")

else:
    print("=> Distinction") 