import os
import pickle as PI

ParamsDI = {'artinx':'',
##           'dna':'C:\\Il\\0__GRM\\BCLymphoma\\RituximabLymphoma\\Abstracts\\',
##            'dna':'C:\\Il\\Amorpha\\RituximabLymphoma\\Abstracts\\',
##            'dna':'C:\\Il\\LI\\TuberculinTestConversion\\',
            'dna':'C:\\Il\\LI\\Bevacizumab\\',
            'target_dna':'',
            'raw':''
             }       

DI = {}

def DumpDI():
    
    dna = ParamsDI['target_dna']
    fna = dna +'/'+'AuthorsTitles.li'
    fi = open(fna, 'wb')
    PI.dump(DI, fi)
    fi.close()
    print 'DumpDI: done'

            
    

def Read__article():

    artinx = ParamsDI['artinx']
    fname = artinx + '.html'
    dna = ParamsDI['dna']
    fna = dna + '/' + fname
    fi = open(fna, 'r')
    line = fi.read()
    ParamsDI['raw'] = line
    DI[artinx] = {}
    fi.close()
    
def Get__title():

    artinx = ParamsDI['artinx']
    #DI[artinx]['authors'] = []
    line = ParamsDI['raw']
    start = line.find('<h1>')     
    end = line.rfind('</h1>')
#    print start, end
    title = line[(start+4):end]
#    print title 
    DI[artinx]['title'] = title
    

    
def GetAuthors():

    artinx = ParamsDI['artinx']
    DI[artinx]['authors'] = []
    line = ParamsDI['raw']
    sl = line.split('cauthor_uid=')[1:-1]
    for ls in sl:
        ls = ls.split('</a>')[0]
        ls = ls.split('">')[1]
        if len(ls) < 25:
            DI[artinx]['authors'].append(ls)
        else:
            print len(ls), 'is too long!'


def AnalyzeOneArticle():

    Read__article()
    Get__title()
    GetAuthors()

    print ParamsDI['artinx'], 'was analyzed'
    
def AnalyseAll():

    dna = ParamsDI['dna']
    flist = os.listdir(dna)#[:5]
    for fna in flist:
        artinx = fna.split('.')[0]
        ParamsDI['artinx'] = artinx
        AnalyzeOneArticle()       
    
def Start():

##    artinx = '15613695'    
##    Read__article(artinx)
####    GetAuthors(artinx)
####    print DI[artinx]['authors']
##    Get__title(artinx)
    AnalyseAll()
    DumpDI()
##    for k, v in DI.items():
##        print k
##        print v
##        print ''
##        print '================='

#Start()


    
