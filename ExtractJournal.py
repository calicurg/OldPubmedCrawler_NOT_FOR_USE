import os
import pickle as PI

#dna = 'C:\\Il\\Amorpha\\PubmedCrawler\\CD44\\Expresssionn__title\\SinglePages'
#dna = 'C:\\Il\\Immunology\\CD133\\SinglePages'
dna = 'C:\\Il\\Amorpha\\PubmedCrawler\\pembro_nivo\\SinglePages'

FilesLI = os.listdir(dna)

JournalDI = {}

anchor = 'div class="cit"'

def GetJournals():
    
    for fn in FilesLI:

              
        fna = dna+'\\'+fn
        fi = open(fna, 'r')
        line = fi.read()
        fi.close()

        if anchor in line:
            pos = line.find(anchor)
            line = line[pos:]
            endpos = line.find('</div>')
            fr = line[:endpos]

            altpos = fr.find('alterm=')
            fr = fr[(altpos+8):]
            endbracket = fr.find('">')
            journal = fr[:endbracket]
            seppos = fr.find('</a>')
            pages = fr[(seppos+4):]

            jour_line = journal + pages

            artinx = fn.split('.')[0]
            JournalDI[artinx] = jour_line
            
    ##        print fn
    ##        print fr
    ##        print jour_line
    ##        print ''
    ##        print '========================='
            
    #        inci = line.count(anchor)
    #        print inci, fn
        else:
            print 'NOT FOUND', fn
       
    print ' GetJournals: done'


def DumpJournals():

    fi = open('JournalDI.li', 'wb')
    PI.dump(JournalDI, fi)
    fi.close()
    print 'DumpJournals: done'

def Start():

    GetJournals()
    DumpJournals()
    
Start()    
    
    
    

