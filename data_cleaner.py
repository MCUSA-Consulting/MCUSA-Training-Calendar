import pandas as pd
import json

orig_json = "states_2.json"
new_json = 'mcusa-states.json'

excel_data = pd.read_excel('mcusa_data.xlsx', sheet_name='state_counts', index_col=None)  
print(excel_data.head())

with open(orig_json, 'r') as f:
    data = json.load(f)

for feature in data['features']:
    print(feature['properties']['NAME'])

for feature in data['features']:
    state_name = feature['properties']['NAME']
    for index, row in excel_data.iterrows():
        if state_name == row['State_Full']:
            feature['properties']['Count_Facilities'] = row['Facility_Count']

with open(new_json, 'w+') as f:
    json.dump(data, f, indent=2)