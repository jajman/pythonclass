import pickle

#basic data type
stringValue='abcde'
integerValue=123
floatValue=0.123

a=[1,2,3,4,5]   #list
a1=[1,'a',2,'b',3]  #different types can be listed
b=(1,2,3,4,5)   #tuple
b1=(1,'a',2,'b',3)
c={'a':1,'b':2,'c':3,'d':4,'e':5}   #dictionary

print(a)
print(a1)
print(b)
print(b1)
print(c)
print()
print(a[0])
print(b[1])
print(c['c'])
print()

#tuple cannot be reassigned
'''a[0]=0
b[0]=0
c['a']=0'''

#file I/O for text data
with open('first.txt','wt') as f:
    f.write(stringValue)

string2=''
for i in range(10):
    string2+=str(i)
with open('second.txt','wt') as f:
    f.write(string2)

string2=''
for i in range(10):
    string2+=(str(i)+'\n')
with open('third.txt','wt') as f:
    f.write(string2)

with open('third.txt','rt') as f:
    string3=f.read(5)
print(string3)
print()

with open('third.txt','rt') as f:
    string3=f.readlines()
print(string3)
print()
for i in range(len(string3)):
    string3[i]=string3[i].strip()
print(string3)
print()

#file I/O for binary data
with open('a.bin','wb') as f:
    pickle.dump(a,f)

with open('a.bin','rb') as f:
    a_1=pickle.load(f)

print(a_1)