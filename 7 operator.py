#arithmatic operators
a=6
b=4

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b) #a^b
print("\n")

#relational/comparison operators
a=50
b=20

print(a==b)
print(a!=b)
print(a>=b)
print(a>b)
print(a<b)
print(a<=b)
print("\n")

#assignment operators
num = 10 # =is a assignment operators
num += 10 # += 
print("Num: ",num)

num -= 10 # -= 
print("Num: ",num)

num *= 10 # *= 
print("Num: ",num)

num /= 10 # /= 
print("Num: ",num)

num %= 10 # %= 
print("Num: ",num)

num **= 10 # **= 
print("Num: ",num)
print("\n")

#logial operators

print(not False)
print(not True)
a=50
b=30
print(not(a>b))

val1 = True
val2 = True
print("And operator : " , val1 and val2)
val1 = True
val2 = False
print("And operator : " , (a==b) and (a>b))

val1 = True
val2 = True
print("Or operator : " , val1 or val2)
val1 = True
val2 = False
print("Or operator : " , (a==b) or (a>b))