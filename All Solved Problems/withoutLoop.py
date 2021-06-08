def recurse (n,d=[]):
    limit=n
    if n not in d :
        if n>=0:
            d.append(n)
            return recurse(n-5,d)
        if n<0:
            d.append(n)
            return recurse(n+5,d)
    else:
        if n!=d[0]:
            d.append(n+5)
            return recurse(n+5,d)
        else:
            return d

print(*recurse(16))