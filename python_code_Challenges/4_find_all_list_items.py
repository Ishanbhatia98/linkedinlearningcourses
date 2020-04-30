def find_item(l, v):
    r = []
    for i in range(len(l)):
        if l[i]==v:
            r.append(i)
    return r

print('Enter list:')
l = list(map(int, input().split()))
print('Enter value:')
v = int(input())


print('The indices corresponding to the value are:')
print(*find_item(l,v))
