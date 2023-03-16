# extract ili-dict from evaluated ambiguous ilis
import csv

# convert_valuated_synsets_to_ili_dict("synsets_more_than_one_ili_validated.txt")

def convert_valuated_synsets_to_ili_dict(input_file):
        out = open("out.txt",'w',encoding='utf-8', errors='ignore')
        with open(input_file,'r', encoding='utf-8', errors='ignore') as ili_validations:
            readCSV = csv.DictReader(ili_validations, delimiter='\t')
#            synset_ili_dict={}
            for row in readCSV:
#                print(row)
                synset = row["SYNSET"]
                iliinfo = row["ILIINFO"]
                out.write("'" + synset + "': " + iliinfo)
        out.close()
#                synset_ili_dict[synset]=iliinfo
#        return synset_ili_dict
        
