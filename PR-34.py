print("Задание 1")
a =int (input())
b =int (input())
c =int (input())
d =int (input())
for g in range (c,d+1):
    print('\t'+str(g),end='')
print(end='\n')
for i in range (a,b+1):
    print(str(i)+'\t',end='')
    for j in range (c,d+1):
        print(str(i*j),end='\t')
    print(end='\n')
print("Задание 2")
a = 0
while a<=100:
  a = int (input())
  if a > 100:
    break
  if a<10:
    continue
  print(a)
print("Задание 3")
a = int(input())
b = 0
while a:
    b += a
    a = int(input())
print (b)
print("Задание 4")
a, b = int(input()), int(input())
s = a
while s % a or s % b:
    s += a
print(s)
print("Задание 5")
a = int(input())
b = int(input())
s = 0
c = 0
for j in range (a,b+1):
    if j%3 == 0:
        s = s+j #42
        c = c+1
    j+=1
print(s/c)
print("Задание 6")
a=str(input())
b=a.upper().count('g'.upper())
c=a.upper().count('c'.upper())
print((b/len(a)*100)+(c/len(a)*100))
print("Задание 7")
s = str(input())
l = len(s)-1
c = 1
t = ''
if len(s)==1:
    t = t +s+str(c)
else:
    for i in range(0,l):
        if s[i]==s[i+1]:
            c +=1
        elif s[i]!=s[i+1]:
            t = t + s[i]+str(c)
            c = 1
    for j in range(l,l+1):
        if s[-1]==s[-2]:
            t = t +s[j]+str(c)
        elif s[-1]!=s[-2]:
            t = t +s[j]+str(c)
            c = 1
print(t)
print ("Задание 8")
a = (int(i) for i in input().split())
s = 0
for i in a:
     s += i
print(s)
print ("Задание 9")
s = [ int(i) for i in input().split()]
t = []
l = len(s)-1
k = 0
i = 0
if len(s)==0:
    print(str(0))
else:
    for st in s:
        if len(s)>1:
            if i==0:
                k = s[i+1] + s[-1]
                t.append(k)
            elif i>0 and i<l:
                k=s[i-1]+s[i+1]
                t.append(k)
            elif i==l:
                k = s[i-1]+s[0]
                t.append(k)
        elif len(s)==1:
            k = s[i]
            t.append(k)       
        i +=1
    j = 0
    for st2 in t:
        print(str(t[j])+' ',end='')
        j +=1
print ("Задание 10")
s=[int(i) for i in input().split()]
s.sort()
m=[]
for i in range(len(s)):
    if i>0:
        if s[i]==s[i-1]:
            if s[i] not in m:
                m+=[s[i]]
for i in m:
    print(i, end=" ")
print ("Задание 11")
a1 = int (input())
s= a1
s2 = 0+abs(a1**2)
while s!=0:
    a1 = int(input())
    s = s + a1
    s2 = s2+abs(a1)**2
    if s==0:
        break
print(s2)
print ("Задание 12")
a=int(input())
m=[]
for i in range(a):
    j=0
    while j<i+1:
        m.append(i+1)
        j+=1
    if len(m)>a: break
m=m[0:a]
for i in m:
    print(i, end=" ")
print ("Задание 13")
lst = [int(i) for i in input().split()]
x = int(input())

for i in range(len(lst)):
	if x == lst[i]:
		print(i, end=' ')

if x not in lst:
    print('Отсутствует')
print ("Задание 14")
n = ''
m = []
while True:
    n = str(input()) # ввод строк
    if n == 'end':
        break
    m.append([int(s) for s in n.split()]) 
li, lj = len(m), len(m[0])
new = [[sum([m[i-1][j], m[(i+1)%li][j], m[i][j-1], m[i][(j+1)%lj]]) for j in range(lj)] for i in range(li)]

for i in range (li):
    for j in range (lj):
        print(new[i][j], end =' ')
    print()
print ("Задание 15")
def spiral(n):
    dx,dy = 1,0           
    x,y = 0,0              
    myarray = [[None]* n for j in range(n)]
    for i in range(1,n**2+1):
        myarray[x][y] = i
        nx,ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<n and myarray[nx][ny] == None:
            x,y = nx,ny
        else:
            dx,dy = -dy,dx
            x,y = x+dx, y+dy
    return myarray
 
def printspiral(myarray):
    n = range(len(myarray))
    for y in n:
        for x in n:
            print (myarray[x][y],end=' ')
        print()

n = int(input())
printspiral(spiral(n))
