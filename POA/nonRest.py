def nonrest(a,q,m,ct,n):
    print(f"{ct}\t{a}\t{q}")
    if ct==0:
        if a[0]=='1':
            a=add(a,m)
            if len(a) > n:#to discard any carry
                a = a[1:]
        return f"Quotient={q} deci={int(q,2)}\nRemainder={a} deci={int(a,2)}"
    a,q=ls(a,q)
    print(f"{ct}\t{a}\t{q}\tafter ls")
    print(f"{ct}\t{a}\t{q}\tafter A=A-M")
    if a[0]=='1':
        print('A<0')
        a=add(a,m)
        if len(a) > n:
            a = a[1:]
        print(f"{ct}\t{a}\t{q}\tafter A=A+M")
    else:
        print('A>0')
        a=add(a,comp(m))
        if len(a) > n:
            a = a[1:]
        print(f"{ct}\t{a}\t{q}\tafter A=A-M")
    q=q.replace('_',str(int(not(int(a[0])))))
    return(nonrest(a,q,m,ct-1,n))
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
def ls(a,q):
    a=a[1:]+q[0]
    q=q[1:]+'_'
    return a,q
a=int(input('Enter numerator '))
b=int(input('Enter denominator '))
n=len(bin(max(abs(a),abs(b)))[2:])+1
a = bin(a)[2:].zfill(n-1) #non restoring mein n-1 aaega and restoring mein n
b = bin(b)[2:].zfill(n-1) 
print(f"Q={a},M={b},A={'0'*n},Count={n-1}")
print("Ct\t\tA\t\tQ\t\tAction")
print(nonrest('0'*n,a.zfill(n-1),b.zfill(n-1),n-1,n-1))
