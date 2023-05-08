import csv
email_list1=[]
email_list2=[]
id=[]
zipcode1=[]
zipcode2=[]

#getting the email from accounts.csv as dict
f=open("file1.csv",'r')
reader_obj=csv.DictReader(f)
for i in reader_obj:
    email_list1.append(i['\ufeffEmail'])
# print(email_list1)

#getting the email from orders.csv as dict
f1=open("file2.csv",'r')
reader_obj=csv.DictReader(f1)
for i in reader_obj:
    email_list2.append(i)
    id.append(i['\ufeffId'])
# print(email_list2)

f2=open("output.csv",'w',newline='')
writer=csv.writer(f2)
writer.writerow(['Id','Zipcode'])

index=0

for i in range(len(email_list2)):
    for j in email_list1:
        if email_list2[i] == j:
            writer.writerow([id[index],j])
    index+=1    

# #new file creation
# f2=open("Profiles.csv",'w',newline='')
# writer=csv.writer(f2)
# writer.writerow(['ContactId','Email','Brands'])
# index=0

# #compare
# for i in range(len(email_list1)):
#     index=0
#     for j in email_list2:
#         if(email_list1[i]==j):
#             writer.writerow([contactid_list[i],j,brands_list[index]])
#         index+=1
# for i in range(len(email2_list)):
#     index=0
#     for j in email_list2:
#         if(email2_list[i]==j and j!=''):
#             if(j not in email_list1):
#                 writer.writerow([contactid_list[i],j,brands_list[index]])
#         index+=1
# for i in range(len(email3_list)):
#     index=0
#     for j in email_list2:
#         if(email3_list[i]==j and j!=''):
#             if(j not in email_list1):
#                 writer.writerow([contactid_list[i],j,brands_list[index]])
#         index+=1
# for i in range(len(email4_list)):
#     index=0
#     for j in email_list2:
#         if(email4_list[i]==j and j!=''):
#             if(j not in email_list1):
#                 writer.writerow([contactid_list[i],j,brands_list[index]])
#         index+=1
# for i in range(len(email5_list)):
#     index=0
#     for j in email_list2:
#         if(email5_list[i]==j and j!=''):
#             if(j not in email_list1):
#                 writer.writerow([contactid_list[i],j,brands_list[index]])
#         index+=1
# print(f2.name,"Created")
# f,f1,f2.close()

