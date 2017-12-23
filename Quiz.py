#All rights reserved to @ Tarun Gudipati
#Program is Developed by @Tarun Gudipati and any illegal use of this code is punishable
import random
#n=int(input("Enter upper bound: "))
def each_chunck(stream,seperator):
    buffer=''
    while True:
        chunck=stream.read(4096)
        yield buffer
        break
    buffer +=chunck
    while True:
        try:
            part,buffer=buffer.split(seperator, 1)
        except ValueError:
            break
        else:
            yield part
try:
    file=open("Questions.txt",'r')
    o=open("Options.txt",'r')
except:
    print("Insufficient Access")
    exit(0)
c=[]
op=[]
for chunk in each_chunck(file,seperator='*\n'):
    c.append(chunk)
del c[0]
for chunk in each_chunck(o,seperator='*\n'):
    op.append(chunk)
del op[0]
n=len(op)
s=[0]*n
t=[0]*n
if n==0:
    k=input("No Questions Set in the repository of Questions")
    exit(0)
for i in range(0,n):
    num=random.randint(0,n-1)
    while(s[num]==1):
        num=random.randint(0,n-1)
    s[num]=1
    a=input(str(i+1)+')'+c[num]+'\n'+op[num]+'\n')
    #t[i]=a
#print("You've Chosen: ")
#print(*t)

    
