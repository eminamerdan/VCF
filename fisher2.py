import argparse
import sys
import scipy.stats as stats
import numpy as np
from os.path import basename, join
import math
from operator import attrgetter

#syn_cmatrix: GENE_NAME | NORMAL | TUMOR


def Fisher(argv):
    parser = argparse.ArgumentParser(usage='%(prog)s [options] arg1 arg2',
                                     description='Process vcf files.')
    parser.add_argument('allbut_cmatrix',
                        type=str)
    parser.add_argument('--total_number',
                        type=int,
                        dest='total_number',
                        action='store',
                        default=405)
    parser.add_argument('--out',
                        type=str,
                        dest='out_dir',
                        action='store',
                        default='.',
                        help='path of the output folder')

  
    args = parser.parse_args()
    
    suffix = "_fisher.txt"
    outfname = join(args.out_dir,
                    basename(args.allbut_cmatrix).split(".")[0] + suffix)
                                     
                                     
    with open(args.allbut_cmatrix, 'r') as f:
        of = open(outfname, 'w')
        for line in f:
            columns = map(int, line.split()[1:])
            # [[mut normal, mut tumor], [non-mut normal, non-mut tumor]]
            cmatrix = [[columns[0] + 1, columns[1] + 1],
                       [args.total_number - columns[0] + 1,
                        args.total_number - columns[1] + 1]]
            oddsratio, pvalue = stats.fisher_exact(cmatrix)
                
                
            of.write('{}\t{}\t{}\n'
                     .format(line.strip(),
                             oddsratio,
                             0-math.log(pvalue, 10)))
                             
        

        f.close()
        of.close()



if __name__ == "__main__":
    Fisher(sys.argv[1:])

