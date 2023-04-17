from xml.etree import ElementTree as ET
from lxml import etree
import re
import csv
# from synset_ili_dict import ili_dict
from synset_ili_dict_2 import ili_dict

'''
Add ILI to Ukrajinet
'''

# init global variable 
g_wordDict = None

'''
Access to Wordnet
===
gets a local wordnet file and returns lexicon
which is used by the function get_word_dict(wordnet)
'''

def get_wordnet_lexicon_local(wnfile):
     loc_wn = open(wnfile,"r",encoding="utf-8-sig")
     wntree = ET.parse(loc_wn)
     wnroot = wntree.getroot()
     lexicon = wnroot.find('Lexicon')
     return lexicon

'''
LexEntries
===
Uses function get_wordnet_lexicon_local(wnfile)
to extract all the information in the file (like lemma)
and writes it to a dictionary wordDict = {}
'''

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

def words_in_synset(id):
    lexicon = get_wordnet_lexicon_local(r'../automatic-ukrajinet.xml')
    words = []
    for lexentry in lexicon.iter('LexicalEntry'):
        for sense in lexentry.iter('Sense'):
            if sense.attrib['synset'] == id:
                lemma = lexentry.find('Lemma').attrib['writtenForm']
                words.append(lemma)
    return(words)

'''
Combine Synsets with ILI
'''
# ili_translations = open('translation_table.tsv','r', encoding='utf-8', errors='ignore')

def find_ilis(w):
    with open('translation_table.tsv','r', encoding='utf-8', errors='ignore') as ili_translations:
        readCSV = csv.DictReader(ili_translations, delimiter='\t')
        ili=[]
        definition=[]
        english=[]
        for row in readCSV:
            if w == row['UA_WORD']:
#                print(w + "IST DRIN!")
                ili.append(row["ILI"])
                definition.append(row["UA_DEF"])
                english.append(row["EN"])
        return ili, definition, english
         
         
def combine_synsets_and_ili():
     g_wordDict = get_word_dict(r'../automatic-ukrajinet.xml')
     out = open("out.txt","w",encoding="utf-8-sig")
     synset_ili_dict={}
     for key in g_wordDict:
          wordlist = g_wordDict[key]
          ili_list=[]
          for w in wordlist:
              ili_w, definition_w, english_w = find_ilis(w)
              if len(ili_w) > 0:
                  ili_list.append([ili_w, definition_w, english_w])
          if len(ili_list) > 0:
              if len(ili_list[0][0]) == 1:
                  synset_ili_dict[key]= ili_list[0]
              else:
                  out.write(key + "\t" + str(wordlist) + "\t" + str(ili_list) + "\n") 
     out.close()
     return synset_ili_dict

'''
Add unique ILIs to Ukrajinet
===
First get a one line version
'''

ua_wn = open(r"../automatic-ukrajinet.xml","r",encoding="utf-8")

'''
The following code aims to edit Ukrajinet so that the entries are each on one line 
'''

def format_ukrajinet_oneline():
    lines = ua_wn.readlines()
    ua_wn.close()
    out_ukrajinet = open("ukrajinet_oneline.xml","w", encoding="utf-8")
    for line in lines:
        if re.match(r'^\t*<LexicalEntry', line):
            line = line.strip('\t')
            line = line.strip('\r')
            line = line.strip('\n')
            out_ukrajinet.write(line)
        elif re.match(r'^\t*<Lemma',line):
            line = line.strip('\t')
            line = line.strip('\r')
            line = line.strip('\n')
            out_ukrajinet.write(line)
        elif re.match(r'^\t*<Pronunciation',line):
            line = line.strip('\t')
            line = line.strip('\r')
            line = line.strip('\n')
            out_ukrajinet.write(line)
        elif re.match(r'^\t*<Sense',line):
            line = line.strip('\t')
            line = line.strip('\r')
            line = line.strip('\n')
            out_ukrajinet.write(line)
        elif re.match(r'^\t*</Sense',line):
            line = line.strip('\t')
            line = line.strip('\r')
            line = line.strip('\n')
            out_ukrajinet.write(line)
        elif re.match(r'^\t*<SyntacticBehaviour',line):
            line = line.strip('\t')
            line = line.strip('\r')
            line = line.strip('\n')
            out_ukrajinet.write(line)
        elif re.match(r'^\t*</SyntacticBehaviour',line):
            line = line.strip('\t')
            line = line.strip('\r')
            line = line.strip('\n')
            out_ukrajinet.write(line)
        elif re.match(r'^\t*</LexicalEntry>', line):
            line = line.strip('\t')
            out_ukrajinet.write(line)
        elif re.match(r'^\t*<Synset.*partOfSpeech="[a-z]"/>', line):
            line = line.strip('\t')
            out_ukrajinet.write(line)
        elif re.match(r'^\t*<Synset.*dc:description=".*"/>', line):
            line = line.strip('\t')
            out_ukrajinet.write(line)
        elif re.match(r'^\t*<Synset',line):
            line = line.strip('\t')
            line = line.strip('\r')
            line = line.strip('\n')
            out_ukrajinet.write(line)       
        elif re.match(r'^\t*<Definition', line):
            line = line.strip('\t')
            line = line.strip('\r')
            line = line.strip('\n')
            out_ukrajinet.write(line)
        elif re.match(r'^\t*</Definition', line):
            line = line.strip('\t')
            line = line.strip('\r')
            line = line.strip('\n')
            out_ukrajinet.write(line)
        elif re.match(r'^\t*<Example', line):
            line = line.strip('\t')
            line = line.strip('\r')
            line = line.strip('\n')
            out_ukrajinet.write(line)
        elif re.match(r'^\t*</Example', line):
            line = line.strip('\t')
            line = line.strip('\r')
            line = line.strip('\n')
            out_ukrajinet.write(line)
        elif re.match(r'^\t*</Synset>', line):
            line = line.strip('\t')
            out_ukrajinet.write(line)
        else:
            out_ukrajinet.write(line)
    out_ukrajinet.close()

# Attribute in Synsets verändern, z.B. ili
# change_attribute_in_ss('ukrajinet-4-n','ili','i97809',r"C:\Users\Melanie Siegel\Documents\05_Projekte\Maksym Vakulenko\Wordnet\ILI\ukrajinet_oneline.xml")

def change_attribute_in_ss(synset, att, value, wordnetfile):
        in_wordnet = open(wordnetfile,"r",encoding="utf-8")
        lines = in_wordnet.readlines()
        in_wordnet.close()
        out_wordnet = open(wordnetfile,"w",encoding="utf-8")
        ss_string = '<Synset id="' + synset + '"'
        for line in lines:
            if ss_string in line:
                line = re.sub(att + '="[a-zA-Z0-9]*"', att + '="'+ value +'"', line)
                print(line)
            out_wordnet.write(line)
        out_wordnet.close()

# Definitionen zu einem Synset hinzufügen
# add_definition_to_ss('ukrajinet-4-n','зношування частинок гірських порід через тертя під дією води, вітру або льоду',r"C:\Users\Melanie Siegel\Documents\05_Projekte\Maksym Vakulenko\Wordnet\ILI\ukrajinet_oneline.xml")


def add_definition_to_ss(synset, definition, wordnetfile):
        ua_wn = open(wordnetfile,"r",encoding="utf-8")
        lines = ua_wn.readlines()
        ua_wn.close()
        out_wordnet = open(wordnetfile,"w",encoding="utf-8")
        ss_string = '<Synset id="' + synset + '"'
        definition_string = "<Definition>" + definition + "</Definition>"
        for line in lines:
            if ss_string in line and "<Definition>" not in line:
                if '<Example>' in line:
                    line = line.replace('<Example>', definition_string + '<Example>')
                elif '<SynsetRelation' in line:
                    line = line.replace('<SynsetRelation', definition_string + '<SynsetRelation',1)
                elif '</Synset>' in line:
                    line = line.replace('</Synset>', definition_string + '</Synset>')
                else:
                    line = line.replace('/>', '>' + definition_string + '</Synset>')
                print(line)
            out_wordnet.write(line)
        out_wordnet.close()

# Testen, welche ILIs nicht eindeutig zugeordnet sind (dasselbe ILI in mehreren Synsets)

def test_for_ambiguous_ili():
    ili_list = []
    ambiguous_ilis=[]
    for key in ili_dict:
        ili = ili_dict[key][0][0]
        if ili in ili_list:
            ambiguous_ilis.append(ili)
        else:
            ili_list.append(ili)
    return ambiguous_ilis

# Alle Einträge mit diesem ILI ausgeben

def entries_with_ili(ili):
        for key in ili_dict:
            if ili == ili_dict[key][0][0]:
                words = words_in_synset(key)
                print(key + "\t" + str(words) + "\t" + str(ili_dict[key]))

def give_ambiguous_ilis():
    ambiguous_ilis = test_for_ambiguous_ili()
    for ili in ambiguous_ilis:
        entries_with_ili(ili)
        print("-----------------")

# Definitionen und ILIs für die eindeutigen ILI-Synsets eintragen

def add_to_nonambiguous_synsets():
    ambiguous_ilis = test_for_ambiguous_ili()
    for key in ili_dict:
        ili = ili_dict[key][0][0]
        definition = ili_dict[key][1][0]
        if ili not in ambiguous_ilis:
            change_attribute_in_ss(key,'ili',ili,r"C:\Users\Melanie Siegel\Documents\05_Projekte\Maksym Vakulenko\Wordnet\ILI\ukrajinet_oneline.xml")
            add_definition_to_ss(key,definition,r"C:\Users\Melanie Siegel\Documents\05_Projekte\Maksym Vakulenko\Wordnet\ILI\ukrajinet_oneline.xml")


# Die Version ohne Zeilenumbruch als Pretty Print speichern
# prettyprint_wordnet("ukrajinet_oneline.xml")


def prettyprint_wordnet(wordnet):
    oneline_wordnet = open(wordnet,"r", encoding="utf-8")
    lines = oneline_wordnet.readlines()
    oneline_wordnet.close()
    pretty_wordnet = open(r'../automatic-ukrajinet.xml',"w",encoding="utf-8")
    for line in lines:
        line = line.replace("<Lemma","\n\t<Lemma")
        line = line.replace("<Sense","\n\t<Sense")
        line = line.replace("</Sense","\n\t</Sense")
        line = line.replace("</LexicalEntry>","\n</LexicalEntry>")
        line = line.replace("<SynsetRelation","\n\t<SynsetRelation")
        line = line.replace("<Definition>","\n\t<Definition>")
        line = line.replace("<Example>","\n\t<Example>")
        line = line.replace("</Synset>","\n</Synset>")
        line = line.replace("<SyntacticBehaviour","\n\t<SyntacticBehaviour")
        pretty_wordnet.write(line)
    pretty_wordnet.close()
