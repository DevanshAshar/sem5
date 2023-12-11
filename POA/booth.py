def booth(a,q,q1,m,ct,n):
    print(f"{ct}\t\t{a}\t{q}\t{q1}")
    if ct==0:
        return f"Answer:{a+q} decimal={int(a+q,2)}" if a[0]=='0' else f"Answer is -ve deci={int(comp(a+q),2)}"
    if q[-1]=='1' and q1=='0' :
        a=add(a,comp(m))
        if len(a)>n: #discard any carry
            a=a[1:]
        print(f"{n}\t{a}\t\t{q}\t\t{q1}\t before ars")
    elif q[-1]=='0' and q1=='1' :
        a=add(a,m)
        if len(a)>n:
            a=a[1:]
        print(f"{n}\t{a}\t\t{q}\t\t{q1}\t before ars")
    a,q,q1=ars(a,q,q1)
    return booth(a,q,q1,m,ct-1,n)
def add(a,b):
    maxLen=max(len(a),len(b))
    a=a.zfill(maxLen)
    b=b.zfill(maxLen)
    result=''
    c=0
    for i in range(maxLen-1,-1,-1):
        r=c
        r+=1 if a[i]=='1' else 0
        r+=1 if b[i]=='1' else 0
        result=('1' if r%2!=0 else '0')+result
        c=1 if r>1 else 0
    if c!=0:
        result='1'+result
    return result.zfill(maxLen)
def comp(a):
    cp=''
    for i in a:
        cp+='1' if i=='0' else '0'
    cp=add(cp,'1')
    return cp
def ars(a,q,q1):
    q1=q[-1]
    q=a[-1]+q[:-1]
    a=a[0]+a[:-1]
    return a,q,q1
a=int(input('Enter M '))
b=int(input('Enter Q '))
n=len(bin(max(abs(a),abs(b)))[2:])+1
a = bin(a)[2:].zfill(n) if a>=0 else comp(bin(a)[3:].zfill(n))
b = bin(b)[2:].zfill(n) if b>=0 else comp(bin(b)[3:].zfill(n))
print(f"M={a},Q={b},A={'0'*n},Count={n}")
print("Ct\t\tA\t\tQ\t\tQ1\tAction")
print(booth('0'*n,b.zfill(n),'0',a.zfill(n),n,n))
