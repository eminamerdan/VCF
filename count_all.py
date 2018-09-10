import sys
import csv
import numpy as np
from collections import Counter

ListFun = ["nonsynonymous_SNV","nonframeshift_insertion", "frameshift_insertion","stopgain","stoploss","frameshift_deletion","nonframeshift_deletion"]

def main(filename, mtype=['germline','somatic']):
    pos_gene=4
    pos_mut=5
    pos_type=11
    dict = {}
    with open(filename) as inf:
        reader = csv.reader(inf, delimiter=" ")
        for i in reader:
            gene=i[pos_gene]
            mut=i[pos_mut]
            vtype=i[pos_type]
            if vtype not in mtype: continue
            dict[gene]=dict.get(gene,[0,0,0])
            if mut == "synonymous_SNV":
                dict[gene][0]=1
                continue
            if mut == "nonsynonymous_SNV":
                dict[gene][1]=1
                dict[gene][2]=1
                continue
            if mut in ListFun: dict[gene][2]=1

    return dict


def sum(filename, dictionary):
    count = 0
    count1 = 0
    count2 = 0
    for k, v in dictionary.items():
        dictionary[k]=dictionary.get(k, [0,0,0])
        if dictionary[k][0] == 1:
            count = count + 1
            continue
        if dictionary[k][1] == 1:
            count1 = count1 + 1
            count2 = count2 + 1
            continue
        if dictionary[k][2] == 1:
            count2 = count2 + 1
            continue
    print filename, count, count1, count2
    return sum

if __name__ == '__main__':
    filename=sys.argv[1]
    mtype=['germline','somatic']
    listfiles=open(filename).readlines()
    for f in listfiles:
        filename=f.rstrip()
        dictionary=main(filename, mtype)
        sum(filename, dictionary)

