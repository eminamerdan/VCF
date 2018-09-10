#!usr/bin/env python2.7
import sys


def gene_parser(filename):
	genes = []
	f = open(filename, 'r')

	for line in f:
		line = line.strip()
		genes.append(line)

	f.close()
	counter = 0
	for i in range(len(genes)):
		for j in range(i):
			if genes[i] == genes[j]:
				continue
			else:
				print genes[i] + '|' + genes[j]

	return 


def main():
	filename = sys.argv[1]
	genes_parsed = gene_parser(filename)
	
	return 0


if __name__ == '__main__':
	d = main()
	sys.exit(d)
