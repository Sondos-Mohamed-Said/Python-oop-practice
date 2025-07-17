def valid(email):
    if '@' in email and '.' in email and(email[0] not in ['@','.'] and email[-1] not in ['@','.']):
      #  dot = email.split('@')[1]
        if '.' in email.split('@')[1] and email.split('@')[1][0] != '.': 
           return True
        else : 
           return False
    else:
        return False

def get_domain(mails)  :
    domain = map(lambda mail: mail.split('@')[1] ,mails)
    domain = list(domain)
    return domain
 
# mails =["ali@gmail.com",
#     "@sara@yahoo.com",
#     "mohamed@outlook@.com",
#     "noha@iti.gov.eg"]   
# valid_mails = map(valid,mails)
# print(list(valid_mails))