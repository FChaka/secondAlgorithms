import sys

#Finding duplicates function
def duplicateNumber(array):
    dups = []
    msg = "No duplicates"

    #Iterate through the array
    #Create and populate with the values, another array called "dups"
    #As long as an array element is found in the "dups", we return it
    for i in range(len(array)):
        if array[i] in dups:
            return array[i]
        else:
            dups.append(array[i])
    return msg



arr_num = eval('input("The number of the array elements: ")')
array = []

#Adding to the array
for i in range(int(arr_num)):
    num = int(input("Enter an element..."))
    if num in range(1, 1000001):
        array.append(num)
    else:
        #print("Sorry that number can't be added to the array")
        print("Sorry that number can't be added to the array")
        sys.exit(0)


result = duplicateNumber(array)
print(result)
