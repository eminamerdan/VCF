import csv
import sys
import numpy as np

ListFun = ["nonsynonymous_SNV","nonframeshift_insertion", "frameshift_insertion","stopgain","stoploss","frameshift_deletion","nonframeshift_deletion"]


def getdict(filename,mtype=['germline','somatic']):
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


def dictupdate(sumdic, dic):
    for k, v in dic.items():
        sumdic[k]=sumdic.get(k,np.array([0,0,0]))
        sumdic[k]=sumdic[k]+np.array(v)
    return sumdic





if __name__ == '__main__':
    sumdic = {}
    files=sys.argv[1]
    mtype=['germline','somatic']
    if len(sys.argv)>2: mtype=[sys.argv[2]]
    listfiles=open(files).readlines()
    for f in listfiles:
        filename=f.rstrip()
        dic=getdict(filename,mtype)
        sumdic=dictupdate(sumdic, dic)
    
    for i in sumdic:
        print("{}\t{}\t{}\t{}".format(i,sumdic[i][0],sumdic[i][1],sumdic[i][2]))

