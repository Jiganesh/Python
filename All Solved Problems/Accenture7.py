def countOperations(a):
    n, res = len(a), 0
    te, to = dict(), dict()
    for i in range(n):
        if i % 2 == 0:
            if a[i] not in te:
                te[a[i]] = 1
            else:
                te[a[i]] += 1
        else:
            if a[i] not in to:
                to[a[i]] = 1
            else:
                to[a[i]] += 1
    me , mo, ce, co = -1, -1, -1, -1
    for it in te:
        if te[it] > ce:
            ce = te[it]
            me = it
    for it in to:
        if to[it] > co:
            co = to[it]
            mo = it
    for i in range(n):
        if i % 2 == 0:
            if a[i] != me:
                res += 1
        else:
            if a[i] != mo:
                res += 1
    return res



print(countOperations([3,1,3,2]))
print(countOperations([3,2,2,2,2,1]))
