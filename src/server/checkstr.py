id1=raw_input("Enter College Id")
y=list(id1.upper())
i=0
j=0
q=[]
x="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
x=list(x)
st=""
while(i<len(y)):
    p=y[i] in x
    if(p==False):
        q.append(y[i])
    i=i+1
i=0
while(i<len(q)):
    st=st+q[i]
    i=i+1
id=int(st)
print(id)
print(type(id))
