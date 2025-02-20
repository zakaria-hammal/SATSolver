def moms(fn : list[list[int]]) -> int: 
    if fn == []:
        return

    c = fn.copy()
    l = c.pop().__len__()

    for a in c:
        if l > a.__len__():
            l = a.__len__()
        
    c = []
    c = [a.copy() for a in fn if a.__len__() == l]

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
        # We eliminate redandent and empty sub-formulas
        res = []
        for val in f:
            if val not in res:
                res.append(val)

        f = res.copy()
        res = [a.copy() for a in f if a != []]
        f = res.copy()

        ens = [a.copy() for a in f]

        # First Step : Unit propagation 
        # We look for litterals which are negations of others litterals in our formula
        l = [(c, d) for c in f for d in f if c.__len__() == 1 == d.__len__() and c[0] == -d[0]]

        # If the list is not empty which mean that there is a litteral and its negation then our formula is unsatisfied
        if(l != []):
            return False

        l.clear()

        # We look for litterals
        l = [c for c in f if c.__len__() == 1]
        c = []

        if l != []:
            # We eliminate rednadent and empty sub-formulas
            for a in l:
                res = []
                for val in f:
                    if val not in res:
                        res.append(val)

                f = res.copy()
                res = [d.copy() for d in f if d != []]
                f = res.copy()

                c = f.copy()

                # Foreach litteral l :
                for b in f:
                    if b.__len__() > 1:
                        # We delete the occurences of -l in each formula :
                        if -a[0] in b:
                            b.remove(-a[0])
                        # We delete the formulas that contains l :
                        if a[0] in b:
                            c.remove(b)
                
                f = c.copy()
                f.remove(a)

                # We search for inconsistancy again
                l1 = [(c, d) for c in f for d in f if c.__len__() == 1 == d.__len__() and c[0] == -d[0]]

                if(l1 != []):
                    return False
            
            res = []
            for val in f:
                if val not in res:
                    res.append(val)

            # We eliminate rednadent and empty sub-formulas
            f = res
            res = [a.copy() for a in f if a != []]
            f = res

            # If our new formula is empty then it is satisfied
            if f == []:
                return True

        else:
            # Second Step : Pure literal elimination

            u = []
            for a in f:
                u = list(set(a).union(u))
            
            # We seach for pure literals
            c = [a for a in u if not -a in u]

            # For all pure ltteral l ...
            for a in c:
                d = [e.copy() for e in f]

                # We delete the clause that contains l :
                for b in f:
                    if a in b:
                        d.remove(b)
                
                f = [e.copy() for e in d]
            
            # If our new formula is empty then it is satisfied
            if f == []:
                return True
    
    # Third Step : Consensus

    # We search for the consensus using MOMS method
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
