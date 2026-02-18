from sql_query_running import *
import pandas as pd


###########################################################################3
def extract_columns_name_from_db_table(table):
    query_result = run_sql_query_for_validation(f'''
       select column_name from information_schema.columns where table_name = '{table}'

      ''')
    actual_columns = []
    for i in query_result:
        actual_columns.append(i[0])
    return actual_columns
#print(extract_columns_name_from_db_table('DimScenario'))

def extract_columns_name_from_Mapp_Doc(table):
    column_list_raw = pd.read_excel("Mapping_Document.xlsx",sheet_name=table)
    column_list = column_list_raw['Target Column'].tolist()
    return column_list
#print(extract_columns_name_from_Mapp_Doc('DimScenario'))
###################################################################33
#check the column name and data type
def check_column_name_and_data_type(table):
    quer_result = run_sql_query_for_validation(f'''
        select Column_name, Data_type 
        from information_schema.columns 
        where table_name = '{table}'
    ''')
    actual_schema = []
    for i in quer_result:
        actual_schema.append({
            "column_name" : i[0],
            "Data_Type" : i[1]
        })
    return actual_schema
#print(check_column_name_and_data_type('DimScenario'))


def extract_columns_and_datatype_from_Mapp_Doc(table):
    # Load the specific sheet for the table
    df = pd.read_excel("Mapping_Document.xlsx", sheet_name=table)

    # Filter the dataframe to only include the relevant columns
    # We use 'Target Column' and 'Data Type' based on your Excel headers
    schema_df = df[['Target Column', 'Data Type']]

    # Convert to a list of dictionaries for easy comparison
    # format: [{'column_name': 'ScenarioKey', 'Data_Type': 'int'}, ...]
    mapping_schema = []
    for index, row in schema_df.iterrows():
        mapping_schema.append({
            "column_name": row['Target Column'],
            "Data_Type": row['Data Type']
        })

    return mapping_schema
#print(extract_columns_and_datatype_from_Mapp_Doc('DimScenario'))
