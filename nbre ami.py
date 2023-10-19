N=int(input("enter the first number"))
M=int(input("enter the second number"))
i=2
S1=0
while i<N:
    D= N// i
    if N % i==0 :
        S1=S1+D
    i=i+1 
u=2
S2=0
while u<M:
    D1= M// u
    if M % u==0 :
        S2=S2+D1
    u=u+1
if S1==M and S2==N:
    print("les  2 nbrs sont amis")
else:
    print("les 2 nbrs ne sont pas des amis")
