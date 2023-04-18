from flask import Flask
# from flask_restful import Resource, Api
import xml.etree.ElementTree as ET

def get_wn():
    uk_wn = open(r"automatic-ukrajinet.xml","r",encoding="utf-8-sig")
    wntree = ET.parse(uk_wn)
    wnroot = wntree.getroot()
    lexicon = wnroot.find('Lexicon')
    return lexicon

def get_word_dict():
    lexicon = get_wn()            
    wordDict = {}        
    for synset in lexicon.findall('./Synset'):
        wordDict[synset.attrib['id']] = []
    for lexentry in lexicon.findall('./LexicalEntry'):
        for sense in lexentry.findall('./Sense'):                
            lemma = lexentry.find('Lemma').attrib['writtenForm']
            wordDict[sense.attrib['synset']].append(lemma)
    return wordDict