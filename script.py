def moms(fn : list[list[int]]) -> int: 
    if fn == []:
        return

    c = fn.copy()
    l = c.pop().__len__()

    for a in c:
        if l > a.__len__():
            l = a.__len__()
        
    c = []
    c = [a for a in fn if a.__len__() == l]

    u = []
    for a in c:
        u = list(set(a).union(u))

    occ = []
    i = 0
    for a in u:
        occ.append(0)
        for b in c:
            for d in b:
                if a == d:
                    occ[i] += 1
        
        i += 1
                
    max = 0

    for i in range(1, len(occ)):
        if occ[max] < occ[i]:
            max = i

    return u[max]
    


def davis_putnam(fnc : list[list[int]]) -> bool:
    f = fnc.copy()
    ens = []

    while ens != f:
        res = []
        for val in f:
            if val not in res:
                res.append(val)

        f = res.copy()
        res = [a.copy() for a in f if a != []]
        f = res.copy()

        ens = [a.copy() for a in f]

        l = [(c, d) for c in f for d in f if c.__len__() == 1 == d.__len__() and c[0] == -d[0]]

        if(l != []):
            return False

        l.clear()

        l = [c for c in f if c.__len__() == 1]
        c = []

        if l != []:
            for a in l:
                res = []
                for val in f:
                    if val not in res:
                        res.append(val)

                f = res.copy()
                res = [d.copy() for d in f if d != []]
                f = res.copy()

                c = f.copy()

                for b in f:
                    if b.__len__() > 1:
                        if -a[0] in b:
                            b.remove(-a[0])
                        if a[0] in b:
                            c.remove(b)
                
                f = c.copy()
                f.remove(a)
                l1 = [(c, d) for c in f for d in f if c.__len__() == 1 == d.__len__() and c[0] == -d[0]]

                if(l1 != []):
                    return False
            
            res = []
            for val in f:
                if val not in res:
                    res.append(val)

            f = res
            res = [a.copy() for a in f if a != []]
            f = res

            if f == []:
                return True

        else:
            u = []
            for a in f:
                u = list(set(a).union(u))
            
            c = [a for a in u if not -a in u]

            for a in c:
                d = [e.copy() for e in f]

                for b in f:
                    if a in b:
                        d.remove(b)
                
                f = [e.copy() for e in d]

            if f == []:
                return True
    
    cons = moms(f)
    f1 = f.copy()
    f1 = [b.copy() for b in f if not -cons in b]

    for b in f1:
        if cons in b:
            b.remove(cons)
    
    if davis_putnam(f1):
        return True
    
    f1 = []
    f1 = f.copy()

    f1 = [b.copy() for b in f if not cons in b]
    for b in f1:
        if -cons in b:
            b.remove(-cons)

    if davis_putnam(f1):
        return True

    return False
