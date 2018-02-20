import sys
import re
def parse_vcf('colon.hg19_multianno.vcf')
    pattern=re.compile(r'"([^;]*)"' , 'Gene.refGene')
	  f=open('colon.hg19_multianno.vcf' , 'r')
	  for line in f:
		  if pattern.search(line):
			  f.write(line)
			  continue

return vcf

if __name__=='__main__':
	vcf=sys.argv[1]
