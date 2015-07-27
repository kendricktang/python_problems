import re

def reversewords(words, f):
    words.reverse()
    f.write(' '.join(words))
    f.write('\n')

def reversewords_printoutput(filename):
    fout=file('b-output.dat', 'w')
    f = file(filename)
    cases=  int(re.compile('([0-9]+)').findall(f.next())[0])
    for x in xrange(cases):
        line = f.next().strip('\n').split(' ')
        fout.write('Case #%d: ' % (x+1))
        reversewords(line, fout)