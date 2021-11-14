import urllib as UL

primer = 'http://www.ncbi.nlm.nih.gov/pubmed/'

Accs = {0:[], ##link inxx
        1:[], 
        2:[], 
        3:[],
        4:[],
        5:[]
        }

dna = ''
linxx__fna = ''

def Get__page(inx):

#    dna = 'C:\\Il\\LI\\LatentTB\\Abstracts'
#    dna = 'C:\\Il\\LI\\BCLymphoma\\Abstracts'
####    dna = 'C:\\Il\\LI\\TuberculinSensitization'
####    dna = 'C:\\Il\\LI\\Bevacizumab'
#    dna = 'C:\\Il\\LI\\TuberculinTestConversion'
    ul_inx = Accs[0][inx]
    
    ul = primer + ul_inx
    try:
        fi = UL.urlopen(ul)
        uline = fi.read()
        fi.close()

        fna = dna + '\\' + ul_inx + '.html'
        fi = open(fna, 'w')
        fi.write(uline)
        fi.close()

        print 'written:', inx
    except:
        print 'NOT DONE:  ', inx
    
def Get__all():

    for y in range(len(Accs[0])):
        
        Get__page(y)

    print 'Get__all: done'
        

def ReadLinxx():
    
    fi  = open(linxx__fna, 'r')
##    fi  = open('Linxx.txt', 'r')
    rl = fi.readlines()
    fi.close()
    for ls in rl:
        ls = ls.strip()
        Accs[0].append(ls)
        
    print 'ReadLinxx: done'    
    
    
def Start():
    ReadLinxx()
#    Get__page(0)
    Get__all()

#Start()   








    
