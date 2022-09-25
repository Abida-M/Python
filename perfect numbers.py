n=int(input("enter number"))
s=0
c=1
while(c<n):
    if(n%c==0):
        s=s+c
    c=c+1
if(s==n):
    print("Perfect number")
else:
	print("Not a Perfect number")
