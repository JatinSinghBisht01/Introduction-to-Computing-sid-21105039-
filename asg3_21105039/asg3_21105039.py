                                   #Assignment 3
# Q1
print("Question 1",'\n')

def counts():
    string=input("enter the string:")
    string1=string.lower()
    temp= string1.split()       # storing each word of string in a temporary list and conerting it to lowercase.
 # storing word and their occurrence in dictionary.
    count={}                  
    for word in temp:
        count[word]= temp.count(word)
    return count
print("word count is :",counts(),'\n')


def charcount():
    string2=input("enter the string:")
    temp2= string2.lower() # storing string into another variable with converting string into lowecase
#storing char and their occurence in dictionary.
    count1={}                 
    for char in temp2:
        count1[char]=temp2.count(char)

    return count1

print("char count is :",charcount(),'\n')

print("Question 2")
#Taking input from user
day=int(input("Enter Day  "))
month=int(input("Enter Month from (1-12)[where january is 1 and december is 12 and similarly rest ] "))
year=int(input("Enter Year "))


#Removing all the invalid cases
if day>30 and month in {2,4,6,9,11}:  #conditioning dates exceeding 30 in feb,april,june,sept and nov
    condition=False
elif day>31 and month in {1,3,5,7,8,10,12}:   # generating error if day>31.
    condition=False
elif (day==29 or day==30) and month==2 and year%4!=0:   # condition get false if day>28  for year other than leap year.
    condition=False
elif day==30 and month==2 and year%4==0:   #limiting dates to 29 in feb in leap year
    condition=False
elif month not in {1,2,3,4,5,6,7,8,9,10,11,12}:  # generating error if month is not in range(1,13)
    condition=False
else:
    condition=True


# checking the condition if false or true and executing its application.
if condition:
    #checking and changing for new year
    if day==31 and month==12:
        n_year=year+1   #entering new year after 31 dec
    else:
        n_year=year   
    if month==12 and day==31:
        n_month=1   #setting the new month to be jan in new year
    else:
        n_month=month
#changing dates
    #checking for months with 31 days
    if month in {1,3,5,7,8,10,12}:
        if day==31:
            next_day=1
            if month!=12:
                n_month=month+1 #entering new month after 31 date is encountered in above mentioned months
            else:
                n_month=1
        else:
            next_day=day+1
    #checking for the month of february
    elif month==2:
        if year%4==0:    #considering the case of leap year
            if day==29:
                next_day=1
                n_month=3
            else:
                next_day=day+1
        else:
            if day==28:
                next_day=1
                n_month=3
            else:
                next_day=day+1
                    
    #covering all the remaining cases
    else:
        if day==30:
            next_day=1
            n_month=month+1
        else:
            next_day=day+1
    #printing next date
    print(f"\nNext Date is: {next_day}/{n_month}/{n_year}")
else:
    #gives a warning and ends the program
    print("\nThat's not a valid date. \n Enter valid date.",'\n')

#Q3
print("Question 3",'\n')
list1=list(map(int,input("Enter the integers separated by whitespace:").split()))
list2=[]    
#storing integers and their square in a tuple with format(i,i**2).
for i in list1:
    tuple1=(i,i**2)
    list2.append(tuple1)
print("The list of integers entered by the user is :",'\n',list1,'\n',
    "The list of tuple consisting integers with their square is:",'\n', list2, '\n')



#Q4
print("Question 4",'\n')
grade_point=int(input("Enter grade points in range [4,10]. Only integral value to be entered:"))
#storing result corresponding to grade_point as dictionary
score={10:"Your grade is 'A+' and Outstanding performance.",
     9:"Your grade is 'A' and Excellent performance.",
     8:"Your grade is 'B+' and Very Good performance.",
     7:"Your grade is 'B' and Good performance.",
     6:"Your grade is 'C+' and Average performance.",
     5:"Your grade is 'C' and Below Average performance.",
     4:"Your grade is 'D' and Poor performance."}
#for grade_point entered in given range.
if 4<=grade_point and grade_point<=10:
    result=score.get(grade_point)
    print(result, '\n')
else:
#for grade_point entered out of given range.
    print("ERROR",'\n', "Enter grade_point in range [2,10]",'\n')


#Q5
print("Question 5",'\n')

# Printing the following pattern :
#   ABCDEFGHIJK           # Row = 6
#    ABCDEFGHI            # Column = 11
#     ABCDEFG
#      ABCDE
#       ABC
#        A

elements = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
# we can use elements.sort() if the list is not in sorted manner by default.

# applying condition on rows to be in pattern.
for row in range(0,6):   
    column=0
    position=0
    # applying condition on columns to be in pattern started from n=11 to n-1 and so on.
    while column<11: 
        if column<row or column>11-row-1:
            print(" ", end="") # printing whitespace at start and end of pattern.    

        else:
            print(elements[position], end="") # printing required elements from list as per pattern. 
            position=position+1
        column=column+1
    print("",)
print('\n')

#Q6
print("Question 6 \n")
data = {} # empty dictionary for storing data.
data1 ={}

enquire="Y" # variable which tell whether user is interested to add data or not.
while (enquire == "Y" or "y") :
    print("enter you data : ")
    sid = int(input("enter student sid (positive value and should be unique) : "))
    s_name = input("enter Student Name(capitalize first letter ) : ") # capitalise first letter of name or we can use s_name.capitalize()
    if (sid<0):
        print("value error.",'\n', " enter positve value only",'/n')
    else:
         # Updating the data in data and daata1
        data.update({sid: s_name})
        data1.update({s_name:sid})
        # Asking if want to enter more input or not
        enquire = str(input("Enter 'Y' to continue or 'N' to end:")) # asking user whether to add more data or not.
    if (enquire=="N" or enquire=="n"):
        break


#printing the data
print("\nQuestion 6(a)")
print("The Data as {'SID':'Name'} is : ")
print(data)

#sorting data by s_name.
print("\nQuestion 6(b)")
list_a=sorted(data1)
dic_1={}
for char in list_a:
    dic_1.update({data1.get(char):char})
print("The data sorted by  s_name:")
print(dic_1)

#sorting data by  SID
print("\nQuestion 6(c)")
sort_dic = sorted(data)
dic_2 = {}
for i in sort_dic:
    dic_2.update({i: data.get(i)})  # iterating in dictionary
print("The Dictionary after sorting according to SID:")
print(dic_2)


print("\nQuestion 6(d)")
enter_sid = int(input("Enter SID to get name of student:"))
# searching and printing the name corresponding to sid entered by user.
output_name = str(data.get(enter_sid))
print(" Name of the student with sid ", enter_sid, " is ", output_name,'\n')


#Q7   
print("Question 7",'\n')

# Printing pattern : 0 1 1 2 3 5 8 13 .........

n_terms=int(input(" enter n (for all n>1) upto which fibonaccai terms to be printed "))

# assigning values to the first two elements of sequence.
n_1=1
n_2=0
n=0
# sum of first two elements of sequence
sum=n_1+n_2

print(f"Fibonnaci sequence upto ", n_terms, "terms :")
print(n_2,end=" ")
print(n_1,end=" ")

#Printing the remaining fibonnaci terms
while n<n_terms-2:        
    n0=n_2+n_1
    n_2=n_1
    n_1=n0
    print(n0,end=" ")
    n=n+1
    sum+=n0
average=sum/n_terms
print('\n',"Average of fibonaccai sequence upto " , n_terms ," terms : " , average,'\n')


 #Q8
print("Question 8",'\n')
set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}

print("Question 8(a)",'\n')
# union set of  set1 and set2 excluding elements common in both sets.
set4= (set1|set2) - (set1 & set2)    # (set1 or set2) - (set1 & set2)
print("(set1 or set2) - (set1 & set2) : ")
print(set4, '\n')

print("Question 8(b)",'\n')
# set of all elements that are in only one of the three sets Set1,Set2 and Set3.
set5 = ((set1|set2|set3) - (set1 & set2) - (set2 & set3) - (set3 & set1))
print("(set1 or set2 or set3) - (set1 & set2) - (set2 & set3) - (set3 & set1) : ")
print(set5, '\n')

print("Question 8(c)",'\n')
# set of elements that are exactly two of the sets Set1, Set2,and Set3.
set6= (set1 & set2) | (set2 & set3) |(set3 & set1)
set7= ((set6) - (set1 & set2 & set3)) # here intersection of set1, set2 and set 3 all taken at a time is a null set.
print("((set1 & set2) or (set2 & set3) or (set3 & set1) - (set1 & set2 & set3)) : ")
print(set7, '\n')

print("Question 8(d)",'\n')
# set of all integers in the range 1 to 10 that are not in Set1.
set8=set(range(1,11)) - set1
print("set of all integers in the range 1 to 10 that are not in Set1 :")
print(set8, '\n')

print("Question 8(e)",'\n')
# Create a new set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3.
set9 = set(range(1,11)) - set2  #set of all integers in the range 1 to 10 that are not in Set2.
set10 = set(range(1,11)) - set3 #set of all integers in the range 1 to 10 that are not in Set3.
set11 = (set8 & set9 & set10) #union set of elements from 1-10 not in any of set1, set2 and set3.
print("set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3 :")
print(set11,'\n')







    


    
