# Extract Information from Ukrajinet

# Importe

#from odenet import *
from xml.etree import ElementTree as ET
from lxml import etree
import re

g_wordDict = None

########## Access to Wordnet #######

def get_wordnet_lexicon_local(wnfile):
     loc_wn = open(wnfile,"r",encoding="utf-8-sig")
     wntree = ET.parse(loc_wn)
     wnroot = wntree.getroot()
     lexicon = wnroot.find('Lexicon')
     return lexicon


########## LexEntries ######
def get_word_dict(wordnet):
    lexicon = get_wordnet_lexicon_local(wordnet)            
    wordDict = {}        
    for synset in lexicon.findall('./Synset'):
        wordDict[synset.attrib['id']] = []
    for lexentry in lexicon.findall('./LexicalEntry'):
        for sense in lexentry.findall('./Sense'):                
            lemma = lexentry.find('Lemma').attrib['writtenForm']
            wordDict[sense.attrib['synset']].append(lemma)
    return wordDict  

def words_in_synset(id, wordnet):        
    return(g_wordDict[id])

########### Write Dictionary of synsets and words in a file ###########

def write_synsets_and_words():
     out = open("out.txt","w",encoding="utf-8-sig")
     g_wordDict = get_word_dict('ukrajinet.xml')
     out.write(str(g_wordDict))
     out.close()



    


      
