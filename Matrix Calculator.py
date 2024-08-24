                                          #MATRIX CALCULATOR
import numpy


print("Select the operation do you want to perform")
print("1- Addition")
print("2- Subtraction")
print("3- Scalar Multiplication")

x= int(input("Enter the choice number: "))

#Addition Block
if x==1:

    print("perform addition")
    row = int(input("enter row no. "))
    column= int(input("enter the column no. "))
    arr1 = numpy.zeros((row,column),int)
    arr2 = numpy.zeros((row,column),int)
# Getting input of an array
    for i in range(0,row):
        for j in range(column):
            arr1[i][j]=int(input("enter the value at arr1[%d][%d]" %(i,j)))
    

    for i in range(row):
        for j in range(column):
            arr2[i][j]= int(input("enter the number at arr2[%d][%d]" %(i,j)))

    print("the sum of arr is : ")
    sum = arr1+arr2
    print(sum)

#Subtraction Block
elif x==2:

    print ("Perform Subtraction")
    row= int(input("enter the number of row : "))
    column= int(input("enter the number of column : "))
    arr1 = numpy.zeros((row,column),int)
    arr2= numpy.zeros((row,column),int)
# Getting input of an array
    for i in range(row):
        for j in range(column):
            arr1[i][j]= int(input("enter the number at arr1 [%d][%d]" %(i,j)))

    for i in range(row):
        for j in range(column):
            arr2[i][j]= int(input("enter the number at arr2 [%d][%d]" %(i,j)))

    print("result of this arr : ")
    sub= arr1-arr2
    print(sub)

#Scalar Multiplication Block

elif x==3:

    print("perform scalar multiplication")
    row= int(input("enter the number of row : "))
    column= int(input("enter the number of column : "))
    arr= numpy.zeros((row,column),int)
# Getting input of an array
    for i in range(row):
        for j in range(column):
            arr[i][j]= int(input("enter the number at arr [%d][%d]" %(i,j)))

    element = int(input("enter the scalar element : "))
    print("result of this arr : ")

    arr= arr*element
    print(arr) 

else: print("Not valid")

