# Use for loop to create uniques list and print it!

lst = [ 'red', 'blue', 'yellow', 'black', 'red', 'blue', 'green', 'black', 'blue']

arr = []

for data in lst:

    if data in arr:
 
       continue
 
   arr.append(data)

print(arr)