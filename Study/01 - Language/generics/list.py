import operator
# https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions
# https://www.w3schools.com/python/python_arrays.asp
# https://www.w3schools.com/python/python_arrays.asp

arr = ["Ford", "Volvo", "Volvo"]
arr[2] = "Audi"

'''
print (arr)
print (arr[1])
print (len(arr))
'''

# ---------------------------------
# 1D array:
# ---------------------------------

# Copy
arr2 = arr.copy()

# Clear array
arr2.clear()    

# Insert 
arr.append("Honda")            # first
arr.insert(0, "Tesla")         # first
arr.insert(len(arr), "Dodge")  # last

# Remove 
arr.pop(0)                     # at specified positon
arr.remove("Dodge")            # first with specified value

# Other
arr.reverse()                  # reverse 
y = len(arr)                   # size
x = arr.count("Tesla")         # count specific items

# iterate over array
for item in arr:
    print(item)
    
# Multiply array 1,2,3 become 1,2,3,1,2,3
arr = [1,2,3]
arr = arr * 2

# ---------------------------------
# 2D array:
# ---------------------------------

# Basic example
arr = [ [1,2,3], [4,5,6] ]
print(arr)
print(arr[0][1])
for x in arr:
    for y in x:
        print(y)


# initializing argument lists
list1 = [ 1, 2, 4, 3]
list2 = [ 1, 2, 4, 3]
  
# Comparing lists 
print (operator.eq(list2, list1))
print (operator.contains([1], [1,2,3]))

# Add elements
output = ""
list1 = list()
list1.append([1,2,3])
list1.append([4, 5, 6])
list1.append([7,8,9])
list1.reverse()
for arr1 in list1:
    for item in arr1:
        output += str(item)
    print (output)
    output = ""

# Extend elements (append at the end)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print (list1)

# Slicing lists (like strings)
list1 = [1, 2, 3, 4, 5, 6]
print(list1[0:2])       # 1,2
print(list1[2:4])       # 3, 4
print(list1[:2])        # 1, 2
print(list1[4:])        # 5, 6
print(list1[9:9])       # []
print(len(list1[9:9]))  # size 0

# Remove duplicates (dics cannot duplicate, so use conversion)
list1 = [1, 1, 2, 2, 3, 3]
list1 = list(dict.fromkeys(list1))
print(list1)