import xml.etree.ElementTree as ET

uk_wn = open(r"ukrajinet.xml","r",encoding="utf-8-sig")
wn_tree = ET.parse(uk_wn)
wn_root = wn_tree.getroot()
lexicon = wn_root.find('Lexicon')

def create_wn():
    pass

def retrieve_wn_lex_entries():  
    # Retrieve LexEntries and save to dictionary

    lex_entries_dict = {}

    for entry in wn_root.findall("./Lexicon/LexicalEntry"):
        entry_dict = {}
        entry_dict["Lemma_writtenForm"] = entry.find("./Lemma").get("writtenForm")
        entry_dict["Lemma_partOfSpeech"] = entry.find("./Lemma").get("partOfSpeech")
        senses_list = []
        for sense in entry.findall("./Sense"):
            senses_list.append(sense.get("synset"))
        entry_dict["Sense"] = senses_list
        
        lex_entries_dict[entry.get("id")] = entry_dict
    
    return lex_entries_dict

def retrieve_wn_synsets(): 
    # Retrieve Synsets and save to dictionary
         
    synset_entries_dict = {}

    for entry in wn_root.findall("./Lexicon/Synset"):
        entry_dict = {}
        # entry_dict["Synset_id"] = entry.get("id") - dont need this because the key is already the id
        entry_dict["Synset_ili"] = entry.get("ili")
        entry_dict["Synset_pos"] = entry.get("partOfSpeech")
        for definition in entry.findall("./Definition"):
            entry_dict["Synset_definition"] = definition.text
            
        synset_entries_dict[entry.get("id")] = entry_dict
    
    return synset_entries_dict


def update_wn():
    pass

def delete_wn():
    pass


