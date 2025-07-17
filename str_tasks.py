# 📝 Problem:
#Write a program that counts up the number of vowels [a, e, i, o, u]contained in the string

# ✅ Example:
# Input:Sondos
# Output:2

def get_vowels(x):
    vowels = ['a','e','i','o','u']
    counter = 0
    for i in x:
        if i in vowels:
         counter = counter+1 
    return counter

# --------------------------------------------------------

# 📝 Problem:
# Write a program that prints the locations of first "i" character in any string you added.

# ✅ Example:
# Input:iti
# Output:0

def location_i(x):   
    for y in  range(len(x)):
        if x[y] == 'i':
            return y 
           


# --------------------------------------------------------




# --------------------------------------------------------
# --------------------------------------------------------

