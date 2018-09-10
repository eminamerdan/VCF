import sys

def dictionary(filename):
    d = {}
    lines = open(filename, 'r').readlines()
    length = len(lines[0].split())
    for line in lines:
        sp = line.split()
        d[sp[0]] = sp[1:]
    return d, length-1


def union(args):
    normal = args[0]
    tumor = args[1]
    
    normaldict = {}
    tumordict = {}
    uniondict = {}
    
    normaldict, length_normal = dictionary(normal)
    tumordict, length_tumor = dictionary(tumor)
    
    k_union = set(normaldict.keys()).union(tumordict.keys())
    

    for k in k_union:
        l1 = tumordict.get(k, [])
        if len(l1) != length_tumor:
            l1 = length_tumor * [0]
        
        l2 = normaldict.get(k, [])
        if len(l2) != length_normal:
            l2 = length_normal * [0]
        
        
        print k, " ".join(list(map(str, l1))), " ".join(list(map(str, l2)))
    
    return uniondict


if __name__ == "__main__":
    union(sys.argv[1:])
