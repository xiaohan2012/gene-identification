import re

def voss(sequence):
    u = {}
    elements = ["A","T","C","G"]
    for ele in elements:
        u[ele] = map(int,re.sub(r"[^%s]" %ele,"0",sequence).replace(ele,"1"))
    return u

if __name__ == "__main__":
    sequence = "ATCGTACTG"
    print voss(sequence)
