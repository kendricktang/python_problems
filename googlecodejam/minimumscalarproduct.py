import re
import numpy as np

def minimumscalarproduct(x, y, f):
    x.sort()
    y.sort()
    y = y[::-1]
    f.write(str(x.dot(y)))

def minimumscalarproduct_printoutput(filename):
    fout = file('c-output.dat','w')
    f = file(filename)
    cases = int(re.compile('([0-9]+)').findall(f.next())[0])
    for x in xrange(cases):
        fout.write('Case #%d: ' % (x+1))
        size = int(re.compile('([0-9]+)').findall(f.next())[0])
        x = np.array(f.next().strip('\n').split(' '), dtype=long)
        y = np.array(f.next().strip('\n').split(' '), dtype=long)
        minimumscalarproduct(x, y, fout)
        fout.write('\n')