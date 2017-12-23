#Question Setter is a property of @Tarun Gudipati Quiz app and any illegal Use of this is punishable
#All Rights Reserved to @Tarun Gudipati
import sys
try:
    f=open("Questions.txt","a")
    o=open("Options.txt","a")
except:
    print("Insufficient access to file")
else:
    choice=input("What you want to do: "+"\n"+"1)Create a Question 2)Exit")
    if choice=='1':
        ch=True
        while(ch):
            print('\n'+"Enter your Question:(Press CTRL+z when done)")
            x=sys.stdin.read()
            print(x+'*',sep='',file=f)
            print('\n'+"Enter the options(Press CTRL+z when done): ")
            x=sys.stdin.read()
            print(x+'*',sep='',file=o)
            c=input("Do you want to set another question:(y/n)")
            if c=='n':
                ch=False
f.close()
o.close()
            
