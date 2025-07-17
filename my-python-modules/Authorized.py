# 📝 Problem:
# You are given a list of users , passwards .check if user is Aouthorized then get pass.

# ✅ Example:
# Input:omar
# Output:Authorized

def check_credintials(DB):
    username = input('enter user name')
    username=username.lower()
    for dic in DB :
        if username == dic['name']:
                Pass = input('enter pass')
            # for Pass in DB:
                if Pass == dic['pass']:
                    print("Authorized") 
                else:
                    print("wrong pass") 
                break    
    else : 
        print("Not Authorized")   
# --------------------------------------------------------       
# 📝 Problem:
# You are given a list of email addresses in the format username@domain Your task is 
# to use the map()function along with a lambda domain part from each email address

# ✅ Example:
# Input:["ali@gmail.com",
#         "sara@yahoo.com",
#         "mohamed@outlook.com",
#         "noha@iti.gov.eg"]

# Output:['gmail.com', 'yahoo.com', 'outlook.com', 'iti.gov.eg'] 


def get_domain(mailss)  :
    domain = map(lambda mail: mail.split('@')[1] ,mailss)
    domain =list(domain)
    return domain
    
# --------------------------------------------------------       
# 📝 Problem:
# You are given a list of email addresses, some of which are invalid.
# Your task is to use the filter() 
# function to return only the valid email addresses.

# ✅ Example:
# Input:["ali@gmail.com",
#     "@sara@yahoo.com",
#     "mohamed@outlook@.com",
#     "noha@iti.gov.eg"]
# Output:['ali@gmail.com', 'noha@iti.gov.eg']


def voicemail_list(email):
    if '@' in email and '.' in email and(email[0] not in ['@','.'] and email[-1] not in ['@','.']):
      #  dot = email.split('@')[1]
        if '.' in email.split('@')[1] and email.split('@')[1][0] != '.': 
           return True
        else : 
           return False
    else:
        return False
   

# --------------------------------------------------------
# 📝 Problem:
# check validation of email entered ,return true if valid, false if not valid .

# ✅ Example:
# Input: @.dd
# Output:not valid try again
def voicemail(email):
    if '@' in email and '.' in email and(email[0] not in ['@','.'] and email[-1] not in ['@','.']):
      #  dot = email.split('@')[1]
        if '.' in email.split('@')[1] and email.split('@')[1][0] != '.': 
           return True
        else : 
           return False
    else:
        return False
    
     
# --------------------------------------------------------

# 📝 Problem:
# Ask the user for his name then confirm that he has entered his name(not an empty 
# string/integers). then proceed to ask him for his email and print all this data(Bonus)
# check if it is a valid email or no

# ✅ Example:
# Input: Sondos       if valid  , enter email sondos@ss.com
# Output:email is valid

def check_user_email(username):
  if (not username.isdigit() and  username and username.strip()):
      email = input('enter email')
      if '@' in email and '.' in email and(email[0] not in ['@','.'] and email[-1] not in ['@','.']):
        #  dot = email.split('@')[1]
          if '.' in email.split('@')[1] and email.split('@')[1][0] != '.': 
              print(f'name = {username},email ={email}')
          else:
              print("not valid")
      else:
        print('email is not valid')




# --------------------------------------------------------

# 📝 Problem:
# Ask user for his email , check if it is a valid email or not
# if not valid handle it

# ✅ Example:
# Input: sondos@ss.com
# Output:email is valid

def try_except():
    for i in range(5):
        mail = input('enter email')
        try:
            if voicemail(mail):
                print('email is valid')
                break  #to end loop 
        except:
            print('email is not valid try agian')  
    else:
        raise TypeError  #to show error if trying  5 times wrong
    
try_except()    
