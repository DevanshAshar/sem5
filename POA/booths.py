def booths(a,m,q,q1,ct,n):
    print(f"{ct}\t{a}\t{q}\t{q1}")
    if ct==0:
        return f"Answer is {a+q} ,dec is {int(a+q,2)}" if a[0]=='0' else f"Answer is negative {a+q}, complement is {complement(a+q)},dec is {int(complement(a+q),2)}"
    if q[-1]=='1' and q1=='0':
        a=add(a.zfill(n),complement(m.zfill(n)))
        if len(a)!=n:
            a = a[1:]
        print(f"{ct}\t{a}\t{q}\t{q1}\t before ars")
    elif q[-1]=='0' and q1=='1':
        a=add(a.zfill(n),m.zfill(n))
        if len(a)!=n:
            a = a[1:]
        print(f"{ct}\t{a}\t{q}\t{q1}\t before ars")
    a,q,q1=ars(a,q,q1)
    return booths(a,m,q,q1,ct-1,n)
def add(a,b):
    maxLen=max(len(a),len(b))
    a=a.zfill(maxLen)
    b=b.zfill(maxLen)
    result=''
    carry=0
    for i in range(maxLen-1,-1,-1):
        r=carry
        r+=1 if a[i]=='1' else 0
        r+=1 if b[i]=='1' else 0
        result=('1' if r%2!=0 else '0')+result
        carry=1 if r>1 else 0
    if carry>0:
        result='1'+result
    return result.zfill(maxLen)
def complement(x):
    res=""
    for i in x:
        if i=='1':
            res+='0'
        elif i=='0':
            res+='1'
    result=add(res,'1')
    return result
def ars(a,q,q1):
    q1=q[-1]
    q=a[-1]+q[:-1]
    a=a[0]+a[:-1]
    return a,q,q1
a = int(input("Enter M : "))
b = int(input("Enter Q : "))
n = len(bin(max(abs(a),abs(b)))[2:])+1
a=bin(a)[2:].zfill(n) if a>0 else complement(bin(a)[3:].zfill(n))
b=bin(b)[2:].zfill(n) if b>0 else complement(bin(b)[3:].zfill(n))
print(f"M = {a}, Q = {b}, A={'0'*n}, Count={n}")
print("Ct\tA\t\tQ\t\tQ1")
print(booths('0'*n, a.zfill(n), b.zfill(n), '0', n, n))
