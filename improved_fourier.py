from numpy import *
from collections import defaultdict


def get_n(u):
    n = {}
    for ele,arr in u.items():
        n[ele] = list(where(array(arr) == 1)[0])
    return n

def get_m(n):
    m = defaultdict(list)
    for ele,arr in n.items():
        for item in arr:
            if arr.index(item) == 0:
                m[ele].append(item)
            else:
                m[ele].append(item - arr[arr.index(item)-1])
    return m

def get_U_bk(m,b,k,N):
    x = exp(-2*pi/N*1j)
    #k = complex128(k)
    xk = x**k
    mb = m[b]
    temp = 1 + xk**mb[-1]
    for i in range(0 , len(mb) - 1)[::-1]:
        print i
        temp = temp * xk**mb[i] + 1
    return temp - 1#above calculating adds an extra 1

def get_U(sequence,mapping = None):
    N = len(sequence)
    u = mapping(sequence)
    n = get_n(u)
    m = get_m(n)

    U = defaultdict(dict)
    for k in xrange(0,N):#0~N-1
        for b in u.keys():
            U[b][k] = get_U_bk(m,b,k,N)
    return U,N,u.keys()
if __name__ == "__main__":
    pass
