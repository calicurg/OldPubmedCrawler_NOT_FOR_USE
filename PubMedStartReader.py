
FormLI = ['<b>',
          '</b>'
          ]

Accs = {0:[],
        1:[], ## Title
        2:[], ##  linxx
        3:[],
        4:[],
        5:[]
        }

start_page = ''

def Get__Linxx():

    for y in range(len(Accs[0])):
        ls = Accs[0][y]
#        print ls
        pos = ls.find('"')
        ls = ls[:pos]
        if ls.isdigit() == True:
            Accs[2].append(ls)
            
    print 'Get__Linxx: done'

            

def Get__title():

    for ls in Accs[0]:
        angle_pos = ls.find('>')
        ls = ls[(angle_pos+1):]
        for junk_si in FormLI:
            if junk_si in ls:
                ls = ls.replace(junk_si, '')

        Accs[1].append(ls)
        

def WriteAcc(inx, fname):

    fna = fname+'.txt'
    fi = open(fna, 'w')
    for ls in Accs[inx]:
        ls += '\n'
        fi.write(ls)
        
    fi.close()
    print 'WriteAcc ', inx, ': done'
    

def PrintAcc(inx):
    for ls in Accs[inx]:
        print ls
        print ''
        print '=============='

def Read__start__page():

#    start_page = 'Pubmed\\StartPages\\LTS__0.htm'
#    start_page = 'C:\\Il\\LI\\BCLymphoma\\BCL__01.htm'
#    start_page = 'C:\\Il\\LI\\StartPages\\tuberculin_sensitization.htm'
#    start_page = 'C:\\Il\\LI\\StartPages\\tuberculin_test_conversion.htm'
    #start_page = 'C:\\Il\\LI\\StartPages\\bevacizumab__01.htm'
    fi = open(start_page, 'r')
    line = fi.read()
    fi.close()

    asep = '<a href="/pubmed/'
    al = line.split(asep)
#    print len(al)
    for y in range(1, len(al)):
        ls = al[y]
        pos = ls.find('</a>')
        ls = ls[:pos]
##        angle_pos = ls.find('>')
##        ls = ls[(angle_pos+1):]
##        for junk_si in FormLI:
##            if junk_si in ls:
##                ls = ls.replace(junk_si, '')
        
        Accs[0].append(ls)

    print 'Read__start__page: done'        
        
        
def Start():
    Read__start__page()
    Get__title()

    Get__Linxx()
#    PrintAcc(2)
    WriteAcc(2, 'Linxx')


#Start()
















    


