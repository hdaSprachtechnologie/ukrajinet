import ua_synsets
from ua_synsets import synsets
from nltk.corpus import wordnet as wn
from itertools import islice


out = open('ua_synsets.xml','w',encoding='utf-8')

'''
("1-n")

<Synset id="ukrajinet-1-n" ili="" partOfSpeech="n"/>


'''



for ss in synsets:
    synset_id = 'ukrajinet-' + ss
    pos = ss[-1]
    out.write('<Synset id="' + synset_id + '" ili=""' + ' partOfSpeech="' + pos + '"/>\n')
    
out.close()
