from seq_mapping import  voss 
from improved_fourier import *

from collections import defaultdict 

def get_SNR(sequence,mapping = voss):
    U,N,elements = get_U(sequence , mapping = mapping)
    N = len(sequence)
    #calculating P
    P = defaultdict(int) 
    for i in xrange(0,N):
        for ele in elements:
            temp = U[ele][i]
            P[i] += temp.real**2+temp.imag**2
    #calculating E
    E = sum(P.values())/N
    #getting SNR
    print P.values()
    print P[N/3-1]
    SNR = P[N/3-1]/E
    return SNR

if __name__ == "__main__":
    sequence = "ATCGTACTG"
    print get_SNR(sequence)
