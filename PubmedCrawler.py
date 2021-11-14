import LightLinter as LL
import tkFileDialog as TFD
import PubMedStartReader as PMSR
import crwl
import os
import ExtractAbstract as EXA
import GetAuthors as AUTH

def WriteAbstractsAsSepaarteFiles():

    dna = LL.TKDI['en']['abstract_pages'].get()
    for k, v in EXA.AbstrDI.items():
        fna = dna+'/'+k+'.txt'
        fi = open(fna, 'w')
        fi.write(v)
        fi.close()
        
        
        

    

def SelectAbstractPagesDir():

    dna = TFD.askdirectory()
    LL.TKDI['en']['abstract_pages'].delete(0, TK.END)
    LL.TKDI['en']['abstract_pages'].insert(0, dna)
    

def Get__authors():

    dna = LL.TKDI['en']['single_pages'].get()
    target_dna = LL.TKDI['en']['data_files'].get()
    AUTH.ParamsDI['dna'] = dna
    AUTH.ParamsDI['target_dna'] = target_dna
    AUTH.Start()
    

def Get__abstracts():

    dna = LL.TKDI['en']['single_pages'].get()
    target_dna = LL.TKDI['en']['data_files'].get()
    EXA.DI['dna'] = dna
    EXA.DI['target_dna'] = target_dna
    
    EXA.Start()

    print 'Abstracts extracted to: ', dna
    

TK = LL.TK

def Get__single__pages():

    crwl.dna = LL.TKDI['en']['single_pages'].get()    
    crwl.linxx__fna = os.getcwd() + '\\'+'Linxx.txt'
    crwl.Start()    
    

def ReadStartPage():

    PMSR.start_page = LL.TKDI['en']['path'].get()
    PMSR.Start()

def Select__data__dir():

    dna = TFD.askdirectory()
    LL.TKDI['en']['data_files'].delete(0, TK.END)
    LL.TKDI['en']['data_files'].insert(0, dna)

def Select__dir():
    
    dna = TFD.askdirectory()
    LL.TKDI['en']['single_pages'].delete(0, TK.END)
    LL.TKDI['en']['single_pages'].insert(0, dna)

def Select__file():

    fna = TFD.askopenfilename()
    LL.TKDI['en']['path'].delete(0, TK.END)
    LL.TKDI['en']['path'].insert(0, fna)
    

def CreateForms():

    LL.Create__root('Pubmed Crawler')
    
    LL.Add__one__frame(0, 'root', 1,  1)
    LL.Add__entry('path', 0, 1, 1, 100, 'Arial 10')


    LL.Add__button('select_file', 0, 1, 3, 10, '...')
    LL.TKDI['bu']['select_file']['command'] = Select__file
    
    LL.Add__button('read_start_page', 0, 1, 4, 20, 'Read Start Page')
    LL.TKDI['bu']['read_start_page']['command'] = ReadStartPage

    ####### line 2

    LL.Add__entry('single_pages', 0, 2, 1, 100, 'Arial 10')
    
    LL.Add__button('select_dir', 0,  2, 3,  10, '...')
    LL.TKDI['bu']['select_dir']['command'] = Select__dir

    LL.Add__button('get_single_pages', 0,  2, 4, 20, 'Get single pages')
    LL.TKDI['bu']['get_single_pages']['command'] = Get__single__pages


    LL.Add__entry('data_files', 0,        3,  1, 100, 'Arial 10')
    LL.Add__button('select_data_dir', 0,  3, 3,  10, '...')
    LL.TKDI['bu']['select_data_dir']['command'] = Select__data__dir

    LL.Add__button('get_abstr', 0,        3, 4,  20, 'Get__abstracts')
    LL.TKDI['bu']['get_abstr']['command'] = Get__abstracts

    LL.Add__button('get_authors', 0,        3, 5,  20, 'Get__authors')
    LL.TKDI['bu']['get_authors']['command'] = Get__authors

    LL.Add__entry('abstract_pages', 0,       4,  1, 100, 'Arial 10')
    
    LL.Add__button('select_ap_dir', 0,       4,  3,  10, '...')
    LL.TKDI['bu']['select_ap_dir']['command'] = SelectAbstractPagesDir
    LL.Add__button('get_abs_seppages', 0,    4 , 4,  30, 'Get abstracts as separate pages')
    LL.TKDI['bu']['get_abs_seppages']['command'] = WriteAbstractsAsSepaarteFiles

    
    

    

 ##  Get__abstracts
    
    


def Start():

    CreateForms()
    LL.TKDI['fr']['root'].mainloop()

Start()
