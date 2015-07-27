import re

def storecredit(credit, items, fout):
    ans = [[x,y] for x in xrange(len(items)) for y in xrange(x+1, len(items)) if items[x]+items[y] == credit]
    fout.write(str(ans[0][0]+1)+' '+str(ans[0][1]+1))
    fout.write('\n')

def storecredit_printoutput(filename):
    fout = file('a-output.dat', 'w')
    f = file(filename)
    cases = int(re.compile('([0-9]+)').findall(f.next())[0])
    for x in xrange(cases):
        credit = int(re.compile('([0-9]+)').findall(f.next())[0])
        numofitems = int(re.compile('([0-9]+)').findall(f.next())[0])
        listofitems = re.compile(r'([0-9]+)[ \n]').findall(f.next())
        items = []
        for y in xrange(numofitems):
            items.append(int(listofitems[y]))
        fout.write('Case #%d: ' % (x+1)),
        storecredit(credit, items, fout)
