import sys
import csv
donor=[]
reciepent=[]    
while True:
    
    
        print('\n1. Enter Donor data\n2. Enter Recipient data\n3. Retrieve Donor specific data\n4. Retrieve Recipient specific data\n5. Exit system')
        ch = int(input('\nEnter your choice :'))
        if ch==1:
            print('\nEnter the following details:')
            name=input("Donor name:")
            uid=input("\nUser id:")
            phno=input("\nPhone Number:")
            email=input("\nEmail id:")
            add=input("\nAddress:")
            bg=input("\nBloodGroup")
            age=int(input("\nAge:"))
            with open('bloodbank.csv','a',newline='') as f:
               # fieldnames=['userid','name','phno','email','address','bloodgroup','age']
               thewriter=csv.writer(f)
               thewriter.writerow([uid,name,phno,email,add,bg,age])
               f.close()
            print("\n\nThank You!!New Donor Registered")
        elif ch==2:
            print("\nEnter following details:")
            Rid=input('\nReciepent ID:')
            name=input("Reciepent Name:")
            sex=input("Gender:")
            bg=input("BloodGroup:")
            Hname=input("Hospital Name:")
            with open('reciepent.csv','a',newline='') as R:
                writ=csv.writer(R)
                writ.writerow([Rid,name,sex,bg,Hname])
                R.close()
            print("\n\nDetails recieved!")
        elif ch==3:
             with open('bloodbank.csv','r') as f:
                 reader=csv.reader(f)
                 for row in reader:
                     donor.append(row)
             uid=input('\nDonor id:')
             col=[x[0]for x in donor]
             if uid in col:
                 for x in range(0,len(donor)):
                     if uid==donor[x][0]:
                         print(donor[x])
            
             else:
                 print("\nInvalid Donor ID!!")
             f.close()
            
        elif ch==4:
            with open('reciepent.csv','r') as R:
                reader=csv.reader(R)
                for row in reader:
                    reciepent.append(row)
            Rid=input('\nReciepent ID:')
            col=[x[0]for x in reciepent]
            if Rid in col:
                for x in range(0,len(reciepent)):
                    if Rid==reciepent[x][0]:
                        print(reciepent[x])
            else:
                print('\nInvalid ID')
            R.close()
        elif ch==5:
            print('\n\nThank you for using this system!\n\n')
            sys.exit(1)
        else:
            print("\n\nWrong Choice!! Try Again!!")
            
            
        