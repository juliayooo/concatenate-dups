# THIS SCRIPT ADDS A "NYC Contact" ITEM TO EACH RECORD 

import pandas as pd 
from datetime import date
import csv

# DEFINE FILE PATHS
nyc_filepath = 'data/concat-nyc-contacts.csv'
merges_filepath = 'data/concatenated_records.csv'
output_filepath = 'data/full-data.csv'

with open(output_filepath, mode='w', newline='', encoding='ISO-8859-1') as out_file:
    writer = csv.writer(out_file)
    # CREATE OUTPUT ROWS
    writer.writerow(['Primary Contact ID', 'Concatenated Description', 'Concatenated Relationship to AFH', 'Date'])
     # READING INPUT FILES
    nyc = pd.read_csv(nyc_filepath, encoding='ISO-8859-1')
    merges = pd.read_csv(merges_filepath, encoding='ISO-8859-1')

    for contact in merges['Primary Contact ID'].unique():
        if contact not in nyc['Contact ID'].values:
            writer.writerow([
                              contact,
                              merges.loc[merges['Primary Contact ID'] == contact, 'Concatenated Description'].values[0],
                              merges.loc[merges['Primary Contact ID'] == contact, 'Concatenated Relationship to AFH'].values[0],
                              merges.loc[merges['Primary Contact ID'] == contact, 'Date'].values[0]])
    for contact in nyc['Contact ID'].unique():
        writer.writerow([
                          contact,
                          "",
                          nyc.loc[nyc['Contact ID'] == contact, 'Concatenated Relationship to AFH'].fillna("").values[0],
                          nyc.loc[nyc['Contact ID'] == contact, 'Date'].values[0]])
