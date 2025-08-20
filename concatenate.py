# THIS FILE CONCATENATES TEXT FIELDS FROM MATCHING MERGED RECORDS
import pandas as pd 
from datetime import date
import csv

filepath = 'data/records.csv'
merges_filepath = 'data/merges.csv'
ouput_filepath = 'data/concatenated_records.csv'

with open(ouput_filepath, mode='w', newline='', encoding='ISO-8859-1') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(['Primary Contact ID', 'Concatenated Description', 'Concatenated Relationship to AFH', 'Date'])


    today = date.today().strftime("%Y-%m-%d")

    data = pd.read_csv(filepath, encoding='ISO-8859-1')
    merges = pd.read_csv(merges_filepath, encoding='ISO-8859-1')

    for group in merges.groupby('Duplicate Group'):
        concat_desc  = ""
        concat_afh = ""
        prim_id = ""
        for c_id in group[1]['Contact ID']:
            desc = data.loc[data['Contact ID'] == c_id, 'Description'].fillna("").values
            afh  = data.loc[data['Contact ID'] == c_id, 'Relationship to AFH'].fillna("").values

            if len(desc) > 0:
                concat_desc += desc[0] + " "
            if len(afh) > 0 and (afh[0] not in concat_afh):
                concat_afh += afh[0] + "; "
            # concat_desc += str(str(data[data['Contact ID'] == c_id]['Description'].values[0]) + "\n")
            # concat_afh += str(str(data[data['Contact ID'] == c_id]['Relationship to AFH'].values[0]) + "\n")
            if merges[merges['Contact ID'] == c_id]['Primary Record'].values[0] == 'Primary Record' or merges[merges['Contact ID'] == c_id]['Primary Record'].values[0] == 1:
                prim_id = c_id
        if prim_id == "":
            continue

        writer.writerow([prim_id, concat_desc, concat_afh, today])
