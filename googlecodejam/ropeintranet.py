import re
import numpy as np

def ropeintranet(windows, f):
    windows = sorted(windows)
    overlap = sum(
        1 for i in xrange(len(windows)) 
        for j in xrange(i, len(windows)) 
        if windows[i][1] > windows[j][1])
    print 'overlap: %d' % overlap
    f.write(str(overlap)+'\n')

def ropeintranet_printoutput(filename):
    fout = file('d-output.dat', 'w')
    f = file(filename)
    cases = int(re.compile('([0-9]+)').findall(f.next())[0])
    for x in xrange(cases):
        fout.write('Case #%d: ' % (x+1))
        size = int(re.compile('([0-9]+)').findall(f.next())[0])
        windows = []
        for y in xrange(size):
            vals = np.array(re.compile('([0-9]+)').findall(f.next()), dtype=long)
            windows.append([vals[0], vals[1]])
        ropeintranet(windows, fout)