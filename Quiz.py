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
n=4
s=[0]*n
t=[0]*n
file=open("Questions.txt",'r')
o=open("Options.txt",'r')
op=o.readlines()
op=[x.strip() for x in op]
c=[]
for chunk in each_chunck(file,seperator='*\n'):
    c.append(chunk)
for i in range(0,n):
    num=random.randint(0,n-1)
    while(s[num]==1):
        num=random.randint(0,n-1)
    s[num]=1
    a=input(str(i+1)+')'+c[num]+'\n'+op[num]+'\n')
    #t[i]=a
#print("You've Chosen: ")
#print(*t)

    
