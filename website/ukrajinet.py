import xml.etree.ElementTree as ET

uk_wn = open(r"ukrajinet.xml","r",encoding="utf-8-sig")
wntree = ET.parse(uk_wn)
wnroot = wntree.getroot()
lexicon = wnroot.find('Lexicon')

def create_wn():
    pass

def retrieve_wn():          
    wordDict = {}        
    for synset in lexicon.findall('./Synset'):
        wordDict[synset.attrib['id']] = []
    for lexentry in lexicon.findall('./LexicalEntry'):
        for sense in lexentry.findall('./Sense'):                
            lemma = lexentry.find('Lemma').attrib['writtenForm']
            wordDict[sense.attrib['synset']].append(lemma)
    return wordDict

def update_wn():
    pass

def delete_wn():
    pass


