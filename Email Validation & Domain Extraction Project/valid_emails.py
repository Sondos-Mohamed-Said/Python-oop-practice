import pandas as pd
import csv
import validation
file = open("E-mails.csv",encoding='utf-8')
f = csv.reader(file)

emails =[]
next(f) # to skip first row (header)
for row in f:
      emails.append(row[3])
valid_emails = list(filter(validation.valid, emails))
#print(valid_emails)
v_emails = open("v_emails.csv",'w',newline='')
writer =csv.writer(v_emails)

#email_domain =[]
for email in valid_emails:  
     #   writer.writerow([email])
        domains = list(validation.get_domain(valid_emails))
        unique_domains = set(domains) # set for return unique (not duplicates)
        writer.writerow([email])
        print(sorted(unique_domains))         
v_emails.close()
