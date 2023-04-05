import uuid
import random
from random import *
import wordlists
from wordlists import wordlists
# from nltk.corpus import wordnet as wn

'''
XML für LexicalEntry erzeugen:
	- Wort-ID erzeugen
	- POS aus der Sense ID nehmen (ggf. korrigieren, wenn nicht plausibel, weil z.B. kleingeschrieben aber N)
	- Sense ID erzeugen aus Wort-ID und Synset-ID
	- XML-Ausgabe
'''

outfile = open('utils/output_files/ua_xml_lexentries.xml','w', encoding="utf-8")

wordid = 0


'''
Input:
[('спотво́рення', 'ukrajinet-1-n'), ('спотво́рення', 'ukrajinet-2796-n')]

Output:
<LexicalEntry id="w1">
    <Lemma writtenForm="спотво́рення" partOfSpeech="n"/>
    <Sense id="w1_1-n" synset="ukrajinet-1-n"/>
    <Sense id="w1_2796-n" synset="ukrajinet-2796-n"/>	
</LexicalEntry>
'''



for wordlist in wordlists:
#   print(wordlist)
    wordid = wordid + 1
    pos = wordlist[0][1][-1]
    outfile.write('<LexicalEntry id="w' + str(wordid) + '">\n\t<Lemma writtenForm="' + wordlist[0][0] + '" partOfSpeech="' + pos + '"/>\n')                  
    for sense in wordlist:
        splitted_sense = sense[1].split("-")
        sense_id = 'w' + str(wordid) + '_' + splitted_sense[1] + '-' + splitted_sense[2]
        outfile.write('\t<Sense id="' + sense_id + '" synset="' + sense[1] + '"/>\n')
    outfile.write('</LexicalEntry>\n')


outfile.close()
