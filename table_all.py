import sys

ListSyn = ["synonymous_SNV"]
ListNonsyn = ["nonsynonymous_SNV"]
ListFun = ["nonsynonymous_SNV","nonframeshift_insertion", "frameshift_insertion","stopgain","stoploss","frameshift_deletion","nonframeshift_deletion"]


def main(filename):
    total_syn=0
    total_nonsyn=0
    total_allbut=0
    with open(filename, 'r') as f:
        for line in f:
            v=line.rstrip().split(' ')
            pos_gene=v[4]
            pos_mut=v[5]
            pos_type=v[11]
            
            if pos_mut in ListSyn:
                total_syn += 1
            if pos_mut in ListNonsyn:
                total_nonsyn += 1
            if pos_mut in ListFun:
                    total_allbut += 1
    
                
    print filename, total_syn, total_nonsyn, total_allbut

if __name__ == "__main__":
    filename=sys.argv[1]
    listfiles=open(filename).readlines()
    for f in listfiles:
        filename=f.rstrip()
        count=main(filename)
        
