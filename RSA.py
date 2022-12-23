import math



def text_trans(t):
    if t == " ":
        return ord(t)-6
    else:
        return ord(t)-65
def e_gcd(a,b):
    if a != 0:
        g,x,y = e_gcd(b % a,a)
        return (g,y - (b // a) * x,x)
    else:
        return (b,0,1)
def bezout(a,m):
    g,x,y = e_gcd(a,m)
    if g == 1:
        return x%m
p=int(input('p = '))

q=int(input('q = '))
n=p*q
print('n =',n)
e=int(input('e = '))
pq=(p-1)*(q-1)


C=[]
M=[]
text=input('original text = ')
d = bezout(e,pq)

print("d =",d)
if math.gcd(e,(p-1)*(q-1)):
    if len(text)%2:
        text+=" "

    
    for i in range(0,len(text),2):
        M.append(text_trans(text[i])*100 + text_trans(text[i+1]))
        
    print("M = ",end="")
    for i in range(len(M)):
        print(M[i],end=" ")
        
    for i in range(len(M)):
        C.append(pow(M[i],e,n))
    #encrypt
    print()
    print("C = ",end="")
        
    for i in range(len(C)):
        print(C[i],end=" ")
    
    #decrypt
    print()
    print("after decoding:",end="")   
    for i in range(len(M)):
        print(M[i],end=" ")
