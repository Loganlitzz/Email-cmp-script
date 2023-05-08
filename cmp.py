import csv
email_list1=[]
email_list2=[]
email2_list=[]
email3_list=[]
email4_list=[]
email5_list=[]
contactid_list=[]
brands_list=[]

#getting the email from accounts.csv as dict
f=open("accounts.csv",'r')
reader_obj=csv.DictReader(f)
for i in reader_obj:
    email_list1.append(i['Email'])
    contactid_list.append(i['contactid'])
    email2_list.append(i['Email2'])
    email3_list.append(i['Email3'])
    email4_list.append(i['Email4'])
    email5_list.append(i['Email5'])
print(email_list1)

#getting the email from orders.csv as dict
f1=open("orders.csv",'r')
reader_obj=csv.DictReader(f1)
for i in reader_obj:
    email_list2.append(i['BillingEmailAddress'])
    brands_list.append(i['Brand'])

#new file creation
f2=open("Profiles.csv",'w',newline='')
writer=csv.writer(f2)
writer.writerow(['ContactId','Email','Brands'])
index=0

#compare
for i in range(len(email_list1)):
    index=0
    for j in email_list2:
        if(email_list1[i]==j):
            writer.writerow([contactid_list[i],j,brands_list[index]])
        index+=1
for i in range(len(email2_list)):
    index=0
    for j in email_list2:
        if(email2_list[i]==j and j!=''):
            if(j not in email_list1):
                writer.writerow([contactid_list[i],j,brands_list[index]])
        index+=1
for i in range(len(email3_list)):
    index=0
    for j in email_list2:
        if(email3_list[i]==j and j!=''):
            if(j not in email_list1):
                writer.writerow([contactid_list[i],j,brands_list[index]])
        index+=1
for i in range(len(email4_list)):
    index=0
    for j in email_list2:
        if(email4_list[i]==j and j!=''):
            if(j not in email_list1):
                writer.writerow([contactid_list[i],j,brands_list[index]])
        index+=1
for i in range(len(email5_list)):
    index=0
    for j in email_list2:
        if(email5_list[i]==j and j!=''):
            if(j not in email_list1):
                writer.writerow([contactid_list[i],j,brands_list[index]])
        index+=1
print(f2.name,"Created")
f,f1,f2.close()

