# THIS SCRIPT ADDS A "NYC Contact" ITEM TO EACH RECORD 

import pandas as pd 
from datetime import date
import csv

# DEFINE FILE PATHS
filepath = 'data/nyc-contacts.csv'
merges_filepath = 'data/concatenated_records.csv'
ouput_filepath = 'data/concat-nyc-contacts.csv'

with open(ouput_filepath, mode='w', newline='', encoding='ISO-8859-1') as out_file:
    writer = csv.writer(out_file)
    # CREATE OUTPUT ROWS
    writer.writerow(['First Name', 'Last Name', 'Contact ID', 'Concatenated Relationship to AFH', 'Date'])
    today = date.today().strftime("%Y-%m-%d")

    # READING INPUT FILES
    data = pd.read_csv(filepath, encoding='ISO-8859-1')
    merges = pd.read_csv(merges_filepath, encoding='ISO-8859-1')
    
    # FOR EACH CONTACT, CHECK IN IN MERGES, CONCATENATE IF SO. 
    for contact in data['Contact ID'].unique():
        concat_afh = ""
        if contact in merges['Primary Contact ID'].values:
            concat_afh_array = merges.loc[merges['Primary Contact ID'] == contact, 'Concatenated Relationship to AFH'].fillna("").values
            if len(concat_afh_array) > 0:
                concat_afh = concat_afh_array[0]
            
            # HANDLE SEMICOLONS
            if len(concat_afh) > 0:
                concat_afh += ";"
        #  IF NOT IN MERGES, USE EXISTING RELATIONSHIP AND ADD NYC   
        else:
            afh  = data.loc[data['Contact ID'] == contact, 'Relationship to AFH'].fillna("").values
            concat_afh = afh[0]
            # HANDLE SEMICOLONS
            if len(concat_afh) > 0:
                concat_afh += ";"
        if 'NYC Contact' not in concat_afh:
            concat_afh += " NYC Contact"

        # WRITE OUTPUT
        writer.writerow([data.loc[data['Contact ID'] == contact, 'First Name'].values[0],
                          data.loc[data['Contact ID'] == contact, 'Last Name'].values[0],
                          contact,
                          concat_afh,
                          today])
