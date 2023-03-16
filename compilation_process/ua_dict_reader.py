import csv
import nltk
import spacy
from nltk.corpus import wordnet as wn
import uuid
import random
from random import *

out_lex = open('ua-lexentries.txt','w', encoding="utf-8")
out_ss = open('ua-synsets.txt','w', encoding="utf-8")
#no_en_trans = open('no_en_trans.txt','w', encoding="utf-8")
#no_en_ss = open('no_en_ss.txt','w', encoding="utf-8")

#synset_id = 0

def determine_ua_word_pos(lexitem):
    if lexitem.endswith("ти") or lexitem.endswith("тися") or lexitem.endswith("тись"):
        pos='v'
    else:
        pos='n'
    return pos

def determine_ua_pos(lexitem):
    toks = lexitem.split()
    if len(toks) == 1:
        pos = determine_ua_word_pos(lexitem)
    else:
        pos = determine_ua_word_pos(toks[0])
    return pos
        

def lookup_pos(synset_wordlist):
    poslist = []
    for lexitem in synset_wordlist:
#        print(lexitem)
        pos=determine_ua_pos(lexitem)
        poslist.append(pos)
    if len(poslist) == 1:
        pos = poslist[0]
    else:
        if poslist.count(poslist[0]) == len(poslist):
            pos = poslist[0]
        else:
            print("POS unclear: " + str(synset_wordlist) + ": " + str(poslist))
            pos='x'
    return pos




#read the dictionary text file with a csv reader
#with open('openthesaurus-input.txt',newline='',encoding="utf-8") as f:

with open('synonym_list.txt',newline='',encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=';')
    synset_id = 0
    for synset_wordlist in reader:
#        print("synset_wordlist: " + str(synset_wordlist))
        synset_id = synset_id + 1
        pos = lookup_pos(synset_wordlist)
#        print(str(synset_id) + '\t' + str(pos) + '\t' + str(synset_wordlist))
        for word in synset_wordlist:
            out_lex.write('("' + str(word) + '","ukrajinet-' + str(synset_id) +'-' + str(pos) + '"),' + '\n')
#this is the synset information that should go into another file, and later be XML:
        out_ss.write('("' + str(synset_id) + '-' + str(pos) + '"),' + '\n')


out_lex.close()
out_ss.close()
#no_en_trans.close()
#no_en_ss.close()
        
'''#This is how one gets the synset id from WordNet:
ss = wn.synsets('dog')[0]
offset = str(ss.offset()).zfill(8) + '-' + ss.pos()
'''
'''#This is how one gets an English translation of a German word with goslate:
gs = goslate.Goslate()
eng_trans = gs.lookup_dictionary('Wiederaufnahme','en')[0][0][0]
'''
