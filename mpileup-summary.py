import sys

'''Counts the number of mapped reads per base position based on bowtie's mpileup files - python mpileup-summary.py *mpileup.  All resulting files will end in *summary'''

d = {}
for f in sys.argv[1:]:
    for line in open(f):
        dat = line.rstrip().split('\t')
        ref = dat[0]
        loci = int(dat[1])
        base = dat[2]
        count = int(dat[3])
        if ref in d:
            if loci in d[ref]:
                d[ref][loci] = d[ref].get(loci) + count
            else:
                d[ref][loci] = count
        else:
            d[ref] = {loci:count}

for k1 in d.keys():
    fp = open(k1 + ".mpileup.summary", 'w')
    for k2 in sorted(d[k1].keys()):
        fp.write('%s %s %s\n' % (k1, k2, d[k1][k2]))
