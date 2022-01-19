#   Assignment_2

#QUESTION_1


print("QUESTION_1:", end=' \n')
string=str(input("Enter the string: "))

#[a] (size of string)
print("(a) Size of string is: ", len(string))

#[b] (reverse string)
string1=string[::-1]
print("(b) The reversed string is: ", string1)

#[c] (slicing string)
S=slice(10, 26)
print("(c) String after slicing: ", string[S])

#[d] (replace substring)
a=string.replace('a case sensitive', 'object oriented')
print("(d) Replacing substring: ", a)
#[e] (finding index of substring)
i=string.index('a')
print("(e) The index of 'a' is: ", i)

#[f] (removing spaces from the string)
r=string.replace(' ','')
print("(f) Removing white spaces: ", r, end="\n")

#QUESTION_2
print("QUESTION_2:",end='\n')
Name='ABC'
SID=21105039
Department='XYZ'
CGPA=9.9
print("Hey, %s Here! \nMy SID is %d \nI am from %s department and my CGPA is %f." % (Name, SID, Department, CGPA), end='\n')


#QUESTION_3
print("QUESTION_3:", end='\n')
a=56
b=10
print("a & b=", (a & b))
print("a | b=", (a | b))
print("a ^ b=", (a ^ b))
print("Left shift both a and b with 2 bits : a=",a<<2, "b=", b<<2)
print("Right shift a with 2 bits and b with 4 bits : a=", a>>2, "b=", b>>4)

#QUESTION_4
print("QUESTION_4:", end='\n')
num1=int(input("Enter the 1st number: "))
num2=int(input("Enter the 2nd number: "))
num3=int(input("Enter the 3rd number: "))
if (num1 >= num2) and (num1 >= num3):
   greatest = num1
elif (num2 >= num1) and (num2 >= num3):
   greatest = num2
else:
   greatest = num3

print("The largest number is", greatest, end='\n')
    
#QUESTION_5
print("QUESTION_5:", end='\n')
string=str(input("Enter the string : "))
if "name" in string:
    print("Yes")
else:
    print("No")
print(end='\n')

#QUESTION_6
print("QUESTION_6: (Valid or Unvalid triangle sides)", end='\n')
side_a=int(input("Enter the 1st side of the triangle : "))
side_b=int(input("Enter the 2nd side of the triangle : "))
side_c=int(input("Enter the 3rd side of the triangle : "))
if side_a < side_b+ side_c and side_b < side_a + side_c and side_c < side_b + side_a:
    print("Yes")
else:
    print("No")    
    

