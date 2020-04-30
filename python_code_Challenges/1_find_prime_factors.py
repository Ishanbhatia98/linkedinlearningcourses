def find(n, i=2, l=[1]):
    if n==1:
        return l
    elif i==2:
        if n%2==0:
            l.append(2)
            return find(n//2,i,l)
        return find(n,i+1,l)
    else:
        if n%i==0:
            l.append(i)
            return find(n//i, i)
        return find(n, i+2,l)

n = int(input())
print('The prime factors of n are')
print(*find(n))
