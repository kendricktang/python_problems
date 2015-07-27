import re

def allyourbase(s):
    base = len(set(s))
    if base == 1:
        base = 2
    minval = 1
    vals = {}
    vals[s[0]] = minval
    date = vals[s[0]]*(long(base)**(len(s)-1))
    for index in xrange(1, len(s)):
        if not vals.has_key(s[index]):
            if minval == 1:
                minval = 0
            elif minval == 0:
                minval = 2
            else:
                minval += 1
            vals[s[index]] = minval
        date += vals[s[index]]*(base**(len(s)-index-1))
    return date

def allyourbase_printoutput(filename):
    fout = file('e-output.dat', 'w')
    f = file(filename)
    cases = int(re.compile('([0-9]+)').findall(f.next())[0])
    for x in xrange(cases):
        fout.write('Case #%d: ' % (x+1))
        fout.write(str(allyourbase(f.next().strip('\n')))+'\n')