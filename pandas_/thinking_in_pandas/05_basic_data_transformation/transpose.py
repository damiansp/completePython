import numpy as np
import pandas as pd


patient_list = pd.DataFrame(
    {'id': ['0123', '4567', '89AB'],
     'hist': ['hbp', np.nan, 'lbp']},
    index=['O+', 'B+', 'O-'])
patient_list.index.name = 'blood_type'
print(patient_list)

drug_table = pd.DataFrame({
    'O+': ['ADF', 'GCB', 'RAB'],
    'O-': ['ADF', 'RAB', ''],
    'A+': ['ACB', 'DF',  ''],
    'A-': ['DCB', 'EFR', ''],
    'B+': ['ACE', '',    ''],
    'B-': ['BAB', 'HEF', '']})
print(drug_table)

drug_table = drug_table.transpose(copy=False)
print(patient_list.join(drug_table))
