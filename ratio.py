import sys
import numpy as np

def single(filename):
    d = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.split()
            gene = line[0]
            tumor2 = line[6]
            d[gene]=d.get(gene, tumor2)
            #d[gene] = tumor2
    return d



def pairs(filename, d):
    with open(filename, 'r') as f2:
        for line in f2:
            line = line.replace("|", " ")
            line = line.split()
            pair1 = line[0]
            pair2 = line[1]
            tumor1 = line[3]

            p1 = d.get(pair1,0)
            p2 = d.get(pair2,0)

            #return pair1, pair2, tumor1, p1, p2
            if p1 == 0 or p2 == 0:
                print line


            Pab = float(tumor1)/405
            if Pab == 0.0:
                print line
            else:
                Pa = float(p1)/405
                Pb = float(p2)/405
                ratio = float(Pab)/float(Pa)*float(Pb)
            
            #print "\n",float(Pab), float(Pb), float(Pa), "\n"
            #print ratio
            print pair1, pair2, tumor1, p1, p2, Pab, Pa, Pb, -1*np.log(ratio)/np.log(10)
                


if __name__ == '__main__':
    filename=sys.argv[1]
    file2=sys.argv[2]
    d=single(filename)
    pairs(file2, d)