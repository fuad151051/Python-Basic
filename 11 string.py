str1 ="My name is fuad." #genarally use this
str2 = 'my name is fuad'
str3 = """my name is fuad."""

print(str1,"\n",str2,"\n",str3)

str4="Fuad Hossain Saad.\nWelcome Fuad"
print(str4)
str5="Fuad Hossain Saad.\tWelcome Fuad"
print(str5)

#concatention
print(str1+str2)#add two string

#length of string
print(len(str1))
a="Fuad"
print(len(a))

#indexing of string
print(str1[0])
print(a[0])
#in indexing start with 0 & we cannot change character 

#slicing (Accesing parts of a string)
print(str1[3:6])
print(str1[:10])#o to 10
print(str1[5:])#5 to end

#negative index
b="apple"
print(b[-3:-1])

