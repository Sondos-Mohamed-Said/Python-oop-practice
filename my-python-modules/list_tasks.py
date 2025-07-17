# 📝 Problem:
#Write a program that generate a multiplication table from 1 to the number passed.

# ✅ Example:
# Input:3
# Output:
# 1*1 = 1
# 2*1 = 2
# 2*2 = 4
# 3*1 = 3
# 3*2 = 6
# 3*3 = 9

def get_multiply(x):
    x= int(x)
    for i in range(1,x+1):
        for j in range(1,i+1):
            y = j * i
            print(f"{i}*{j} = {y}")
            
# --------------------------------------------------------            
# 📝 Problem:
#Write a program that generate a list of lists contain multiplication table from 1 to the number passed.

# ✅ Example:
# Input:3
# Output:[[1], [2, 4], [3, 6, 9]]

def multiply_list(num) :   
    num=int(num)
    lst =[]
    for i in range(1,num+1):
        res =[]
        for j in range(1,i+1):
            res.append(i*j)
        lst.append(res)
    return lst

# --------------------------------------------------------       

# 📝 Problem:
# Fill an array of 5 elements from the user, Sort it in descending 
# and ascending orders then display the output.

# ✅ Example:
# Input:1958
# Output:['1', '5', '8', '9']

def sort_list(arr) :
    arr= list(arr)
    arr.sort()
    print(arr)
    arr.sort(reverse=True)
    print(arr)
# --------------------------------------------------------       

