# 📝 Problem:
# Write a program that build a Mario pyramid like below:.

# ✅ Example:
# Input:5
# # Output:
#      *
#     **
#    ***
#   ****
def mario_pyramid(x):
        x= int(x)
        star = '*'
        space = ' '
        for i in range(1,x):
                print (space*(x-i),star*(i))
        

        
# 📝 Problem:
# Write a program that build a Mario pyramid like below:.

# ✅ Example:
# Input:5
# # Output:
# [' ', ' ', ' ', '*', '*']
# [' ', ' ', '*', '*', '*']
# [' ', '*', '*', '*', '*']
# ['*', '*', '*', '*', '*']   



def mario_list(x) :
        x= int(x)
        star = '*'
        space = ' '
        lst =[" "," "," "," "," "]

        for i in range(len(lst)):

                lst.append("*")
                lst.remove(" ")
                print(lst) 
                
       
