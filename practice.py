
# Program to calculate the sum of all numbers from 0 to n
n = int(input("Enter a number to get the sum: "))
sum=0
for i in range(n+1):
    sum=sum+i
print("The sum is: ", sum)

# Program to calculate the factorial of a number n
n = int(input("Enter a number whose factorial you want: "))
if n==0:
    print("The factorial is: 1")
elif n<0:
    print("Factorial is not defined for negative numbers")  
elif n==1:
    print("The factorial is: 1")
else:
    fact=1
    for i in range(1,n+1):
        fact = fact*i
    print("The factorial is: ", fact)

# Program to calculate the sum of first n odd numbers
n = int(input("Enter a number to get the sum of first n odd numbers: "))
sum=0
for i in range(n+1):
    if i%2!=0:
        sum=sum+i
print("The sum of first n odd numbers is: ", sum)

#Remove Duplicates from List
list = [1,2,3,4,5,6,1,2,3,4]
newList = []
for i in list:
    if i not in newList:
        newList.append(i)
print(newList)

#Second Largest Element
list = [1,2,3,4,5,6,1,2,3,4]
for i in list:
    max1 = max(list)
    list.remove(max1)
    max1 = max(list)
print("The second largest element is: ", max1)


#Count frequnecy of elements in a list
n = int (input("Enter number of elements: "))
list =[]
for i in range(n):
     print("Enter element:")
     li = int(input(" "))
     list.append(li)

dict={}
for i in list:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
print("Frequency of each number is", dict)

#Program to check whether two strings are anagrams or reverse of each other.
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1) == sorted(str2):
    print("The strings are anagrams ")
else:
    print("The strings are not anagrams ")
list1 = list(str1)
list2 = list(str2)
if list1[::-1] == list2 or list1[::-1] == list2:
    print("The strings are reverses of each other")
else:
    print("The strings are not reverses of each other")

#Program to print common elements in two lists
list1 = [1,2,3,4,5,6]
list2 = [4,5,6,7,8,9]
set1 = set(list1) 
set2 = set(list2)
commonElem = set1.intersection(set2)
print("The common elements are: ", commonElem)


#Program to print Fibonacci series up to n terms
n = int(input("Enter number of terms in Fibonacci series: "))
if n == 0:
    print("Fibonacci series: 0 ")
elif n==1:
    print("Fibonacci series: 0 ")
else:
    a,b = 0,1
    print("Fibonacci series: ")
    print(a)
    print(b)
    for i in range(2,n):
        c = a + b
        print(c)
        a = b
        b = c

#Rotate List by K Positions
list = [1,2,3,4,5,6,7,8,9]
k = int(input("Enter number of positions to rotate the list: "))    
k = k % len(list) 
rotatedList = list[k:] + list[:k]
print("The rotated list is: ", rotatedList)

#Program to check if a number is prime
n = int(input("Enter a number to find its prime or not:"))
if n==1:
    print("1 is neither prime nor composite")
    if(n==2):
        print("2 is a prime number")
else:
    count=1
    for i in range (1,n//2):
        if(n%i==0):
            count=count+1
        
    if(count>2):
        print(n,"is not a prime number")
    else: 
        print(n,"is a prime number")  

#Dictionary Inversion
dict = {'a': 1, 'b': 2, 'c': 3}
invertDict = {value: key for key, value in dict.items()}
print("The inverted dictionary is: ", invertDict)