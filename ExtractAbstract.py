import os
import pickle as PI

JnkLI = ['<AbstractText ',
         '<AbstractText>',
         'Label=',
         '"NlmCategory="',
         'NlmCategory=',
         '</AbstractText>',
         '</p>',
         '<h4>',
         '</h4>',
         '<p>',
         '"BACKGROUND"',
         '"METHODS"',
         '"RESULTS"',
         '"CONCLUSIONS"',
         "OBJECTIVE",
         "CONCLUSION",
         '"PATIENTS AND METHODS"',
         '"PURPOSE"',
         "INTERPRETATION AND CONCLUSIONS",
         "METHODS AND MATERIALS",
         "MATERIALS AND METHODS",
         '"UNLABELLED"',
         '"">',
         '>'
         ]

SpecDI = {'&lt;':'<',
          '&gt;':'>' 
          }

DI = {0:'',
##      'dna':'C:\\Il\\LI\\BCLymphoma\\Abstracts\\',
##      'dna':'C:\\Il\\LI\\TuberculinSensitization\\',
##      'dna':'C:\\Il\\LI\\TuberculinTestConversion\\',
      'dna':'C:\\Il\\LI\\Bevacizumab\\',
      'target_dna':'',
      'inx':'',
      'zero':0
      }

AbstrDI = {}

def DumpAbstrDI():

    dna = DI['target_dna']
    fna = dna +'/'+'AbstrDI.txt'
    fi = open(fna, 'wb')
    PI.dump(AbstrDI, fi)
    fi.close()

    print 'DumpAbstrDI: done'    


def Write__all():

    dna = DI['target_dna']
    fna = dna +'/'+'AllAbstracts.txt'

    fi = open(fna, 'w')
    for k, v in AbstrDI.items():
        ls = v+'\n'
        fi.write(ls)
        
    fi.close()
    print 'Write__all: done'
        


def ReadFile(fname):
    
    fna = DI['dna'] +'/'+ fname + '.html'
    fi = open(fna, 'r')
    DI[0] = fi.read()
    fi.close()
    DI['inx'] = fname

    

def replace__specials():
    
    ls = DI[0]
    
    for k, v in SpecDI.items():
        if k in ls:
            ls = ls.replace(k, v)

    DI[0] = ls
#    print 'replace__specials', len(ls)


def replace__jnks():

    ls = DI[0]
    
    for si in JnkLI:
        if si in ls:
            ls = ls.replace(si, '')

    DI[0] = ls
#    print 'replace__jnks', len(ls)


def Get__raw__abstract():

    line = DI[0]

    AbPrimer = 'AbstractText'
    StartPrimer = '<'+AbPrimer
    start =  line.find(StartPrimer)
    if start == 0:
        AbPrimer = 'Abstract'
        StartPrimer = '<'+AbPrimer
        start =  line.find(StartPrimer)

    EndPrimer = '</' +AbPrimer+'>'
        
    endpos = line.rfind(EndPrimer)

    ls = line[start:endpos]
#    print 'Get__raw', len(ls)
    DI[0] = ls
    

def Refine():
    replace__jnks()
    replace__specials()
    inx = DI['inx']
    AbstrDI[inx] = DI[0]
#    print ls



def Get__all():
    
    flist = os.listdir(DI['dna'])
    for fna in flist:
        fname = fna.split('.')[0]
        #print fname
        ReadFile(fname)
        Get__raw__abstract()
        if len(DI[0]) == 0:
            DI['zero'] += 1
        else:
            Refine()

            #print '=============================='

    print 'Get__all: done'        

def Start():

##    ReadFile('12123339')
##    Get__raw__abstract()
##    Refine()
#    print DI[0]

    Get__all()
    Write__all()
    DumpAbstrDI()

    print DI['zero']
    
#Start()







