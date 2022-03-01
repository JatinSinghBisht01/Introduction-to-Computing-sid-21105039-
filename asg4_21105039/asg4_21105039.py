# Assignment 4

#Q1

print("Question 1 \n")

# defining a funtion of tower of hanoi named TOH.
def TOH(n_disc, source, auxillary, destination):
    if (n_disc>0):
        TOH((n_disc-1), source, destination, auxillary)              #swapping the values of destination and auxillary container.
        print("Move a disc from",source," to  ",destination)
        TOH(n_disc-1, auxillary, source, destination)                #swapping the values of auxillary and source container.


# calling the function
print(TOH(3,1,2,3))

#Q2

print("\n Question 2 \n")
# printing pascal's triangle that is of following pattern.
#         1
#       1   1
#     1   2   1
#   1   3   3   1
# 1   4   6   4   1

# using recursions.
n = int(input("Enter n upto which pascal triangle is to be printed."))
print("\n Recursive Approach : \n")
def pascal(n, col=n):
    if n<0:
        return "ERROR!, Row can't be negative."
    if n == 0:
        return
    
    pascal(n-1,col)

    #printing the spaces
    print('  '*(col-n), end='')
    #assigning base value as 1 to avoid maximum limit error. 
    val = 1
    for row in range(1, n+1):

        print(val, end ='   ')

        #using Binomial Coefficient
        # nCr = n! / (r! * (n-r)!)
        val = val * (n - row) // row
    print()
pascal(n)

# using iterations.
print("\n Iterative approach : \n")
for row in range(1, n+1):

    # printing spaces.
    print('  '*(n - row), end='') # for ith row ( n - i) th spaces has to be printed.

    cell = 1
    # assigning values to cell on reaching jth column
    for col in range(1, row+1): 
        print(cell, end='   ')

        cell = cell * (row- col) // col
    print()
print("")

#Q3

print("Question 3")

print("Enter value so as int_1 > int_2")
int_1=int(input("Enter integer 1 : "))
int_2=int(input("Enter integer 2 : "))
remainder=int_1%int_2  #calculating remainder.
quotient=int_1//int_2  #calculating quotient.
print("Remainder is: ", remainder)
print("Quotient is: ",quotient)
# checking whether remainder and quotient are non zero.
if(remainder!=0):
    if (quotient!=0):
        print("Both values are non zero")
    else:
        print("quotient is non zero")
else:
    if (quotient!=0):
        print("remainder is zero")
    else:
        print("Both values are zero")
#adding data into set and updating values.
set1=set()
for i in range (4,7):
    a=remainder+i
    b=quotient+i
    if(a>4):
        set1.add(a)
        print(set1)
    if(b>4):
        set1.add(b)
        print(set1)
    else:
        continue

print(set1)
set2=frozenset(set1)
print("Immutable set: ", frozenset(set1))
print("Max value in the set: ", max(set2))
print("Hash value: ", hash(max(set2)))
print("")

#Q4

print("\n Question 4 \n")

# creating class.
class student:
    # initialising the constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    # printing the data.
    def stu_info(self):
        print("Student Name : ", self.name )
        print("Roll No : ", self.roll_no)
    # calling destructor.
    def __del__(self):
        print("Destructor called, data deleted.")

    
#creating object of class
data = student("Jatin Singh Bisht", 21105039)

# calling instance method using object data.
data.stu_info()

# deleting
del data

#Q5

print(" \n Question 5 \n")

# creating a class named Employee
class Employee:
    # initialising the constructor.
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    # printing the data.
    def emp_info(self):
        print("Employee name : ", self.name)
        print("Employee salary : ", self.salary)
    # deleting an employee record.
    #def __del__(self):
    #    del self.name
    #    print("The destructor called, record of %s is deleted. " %self.name)

# creating object of  class.
emp_1 = Employee("Mehak", 40000)
emp_2 = Employee("Ashok", 50000)
emp_3 = Employee("Viren", 60000)

#calling instance method using objects emp_1,emp_2, emp_3.
emp_1.emp_info()
print('\n')
emp_2.emp_info()
print('\n')
emp_3.emp_info()

# updating salary of Mehak.
emp_1.salary = 70000

# Calling the emp_info of emp_1.
print("\nThe updated data of emp_1 is :")
emp_1.emp_info()
print('\n')
# Deleting the records of emp_3( Viren).
del emp_3
print("Record of Viren is deleted.")


#Q6

print("\n Question 6 \n")
George_word = input("Enter George's word.")
Barbie_word = input("Enter Barbie's guessed word.")

# definging a count function to have a check on total chars used.
def charcount(n):
    string=n
    temp= string.lower() # storing string into another variable with converting string into lowecase
#storing char and their occurence in dictionary.
    count1={}                 
    for char in temp:
        count1[char]=temp.count(char)

    return count1

# shopkeeper's statement to check validity of framed word by Barbie.
def validity(statement):
    if (statement == 'y'):
        print("Congratulations!,\n you passed the test!!\n\n")
    elif (statement == 'n'):
        print("Word is not meaningful,\n friendship is fake!!\n\n")
    else:
        print("Invalid input, try again")
        validity()
# verifying the words entered by friends are different.
# checking whether george's and barbies word is framed of same chars.
if charcount(George_word) != charcount(Barbie_word):
    print("ERROR!!! \n Letters are not same \n Friendship is fake.")
# verifying the words entered by friends are different.
elif (George_word == Barbie_word):
    print("ERROR!!! \n Same word \n Enter different word.")
else:
# taking shopkeepr's statement.
    statement = input("\n Is the word meaningful?(y or n)\n")
    validity(statement)
print("")











