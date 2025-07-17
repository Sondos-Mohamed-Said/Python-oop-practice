import str_tasks
import list_tasks
import patterns
import Authorized

x = input('inter a string')        
print(str_tasks.get_vowels(x))
print(str_tasks.location_i(x))

x = input('inter a number') 
print(list_tasks.get_multiply(x))

array = input("enter 5 numbres")
print(list_tasks.sort_list(array))

number = input("enter number")
print(list_tasks.multiply_list(number))


x = input('inter a number')  
print(patterns.mario_pyramid(x))  
print(patterns.mario_list(x)) 


        
Data=[{'name':'omar','pass':'1234'},
    {'name':'David','pass':'564'},
    {'name':'sondos','pass':'555'},
    {'name':'Ahmed','pass':'789'}
    ]
print(Authorized.check_credintials(Data))  



mails =["ali@gmail.com",
        "sara@yahoo.com",
        "mohamed@outlook.com",
        "noha@iti.gov.eg"]     
print(Authorized.get_domain(mails)) 
valid_mails = filter(Authorized.voicemail_list,mails)
print(list(valid_mails))



email = input('enter email')    
while not Authorized.voicemail(email):   
        email = input('not valid try again')
        Authorized.voicemail(email)
print('email is valid')   

username = input('enter user name')
print(Authorized.check_user_email(username))       
print(Authorized.try_except())
