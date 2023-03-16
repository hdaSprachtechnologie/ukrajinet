# extract the necessary information from the translation table

import pandas as pd
import csv

#translation_list_df = pd.read_csv('ILI_Translations_utf8.tsv', sep='\t')

#print(translation_list_df['ILI'])

out = open('out.tsv','w', encoding='utf-8', errors='ignore')

with open('ILI_Translations_utf8.tsv','r', encoding='utf-8', errors='ignore')  as csvfile:
        readCSV = csv.DictReader(csvfile, delimiter='\t')
        list_of_problematic_ilis = []
        for row in readCSV:
            ili = row['ILI']
            en_source = row['SOURCE']
            target_ua = row['TARGET-UA']
            if target_ua.count(":") == 1:
                lemma, definition = target_ua.split(":")
                out.write(ili + "\t" + en_source + "\t" + lemma + "\t" + definition + "\n")
            else:
                list_of_problematic_ilis.append(ili)

print(str(list_of_problematic_ilis))
out.close()
