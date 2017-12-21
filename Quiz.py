import random
#n=int(input("Enter upper bound: "))
n=4
s=[0]*n
t=[0]*n
for i in range(0,n):
    num=random.randint(0,n-1)
    while(s[num]==1):
        num=random.randint(0,n-1)
    s[num]=1
    file=open("Questions.txt",'r')
    o=open("Options.txt",'r')
    c=file.readlines()
    op=o.readlines()
    op=[x.strip() for x in op]
    c=[x.strip() for x in c]
    a=input(str(i+1)+')'+c[num][2:]+'\n'+op[num]+'\n')
    t[i]=a
print("You've Chosen: ")
print(*t)

    
