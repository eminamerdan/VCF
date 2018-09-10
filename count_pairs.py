import sys

def counter(filename):
	d = {}
	with open (filename) as f:
		for line in f:
			line = line.rstrip()
			line = line.split("|")
			if tuple((line[0], line[1])) in d:
				d[tuple((line[0], line[1]))] +=1
			else:
				d[tuple((line[0], line[1]))] = 1
	return d
	

if __name__ == "__main__":
	filename = sys.argv[1]
	total_d= counter(filename)
    of = open(outfname, 'w')
	for key in total_d:
		of.write(print key[0], "|", key[1], "\t" , total_d[key])
    of.close
