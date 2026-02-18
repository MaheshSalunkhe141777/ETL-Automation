from sql_query_running import *
import pytest

from Framework_ETL_Testing import *

#Validate the table available in Database.
def test_availability_of_table():
    assert run_sql_query_for_validation('''
    
    select count(*) from Dimcustomer
    ''')[0][0] >= 0


#Using parametrizing checking multiple tables
@pytest.mark.parametrize('tables',
                         ['DimCustomer','Dimcustomer_Target']

                         )
def test_availability_of_group_of_tables(tables):
    assert  run_sql_query_for_validation( f'''
    
    select * from {tables}
    ''') [0][0] >= 0


#validate presence of data in tables
@pytest.mark.parametrize('tables',
                         ['DimCustomer','Dimcustomer_Target']
                         )
def test_presence_of_data_in_tables(tables):
    assert run_sql_query_for_validation(f'''
   select * from {tables}
     ''') [0][0] >= 1

#validation of column name of tables(Extract column name from tables)
def test_validate_column_name_of_tables():
    # 1. Only select the COLUMN_NAME from SQL
    query_results = run_sql_query_for_validation(f'''
        SELECT COLUMN_NAME 
        FROM information_schema.columns 
        WHERE table_name = 'DimScenario'
    ''')

    # 2. Extract the string from the tuple: (val,) -> val
    # We use result[0] because each row is a tuple
    actual_columns = [row[0] for row in query_results]

    # 3. Compare sorted lists (and remove the extra comma from your expected list)
    expected_columns = ['ScenarioKey', 'ScenarioName']

    assert sorted(actual_columns) == sorted(expected_columns)


#Extract column name from EXCEL sheet for one table.
def test_extract_columns_name_from_mapp_document():
     assert (sorted(extract_columns_name_from_db_table('DimScenario')) ==
     sorted(extract_columns_name_from_Mapp_Doc('DimScenario')))




#Extract data from document for multiple table and compare SQL server tables
@pytest.mark.parametrize('tables',['DimScenario',
                                   'DimReseller'])


def test_extract_columns_name_from_mapp_document(tables):
    assert (sorted(extract_columns_name_from_db_table(tables)) ==
            sorted(extract_columns_name_from_Mapp_Doc(tables)))

#How to check column name and data type


def test_column_name_and_data_type():
    assert ((check_column_name_and_data_type('DimScenario')) ==
            (extract_columns_and_datatype_from_Mapp_Doc('DimScenario')))



#validate the duplicate records
# 1. The first argument is ONE string with comma-separated names
# 2. The second argument is a LIST of TUPLES
@pytest.mark.parametrize('Primer_key, table_name', [
    ('ScenarioKey', 'DimScenario'),
    ('CustomerKey', 'DimCustomer')
])
def test_duplicate_records(Primer_key, table_name): # 3. Arguments must be here!
    query = f'''
        select {Primer_key}, count(*) 
        from {table_name} 
        group by {Primer_key} 
        having count(*) > 1
    '''
    result = run_sql_query_for_validation(query)
    assert result == [], f"Duplicates found in {table_name}: {result}"



#completness testing
def test_completeness_testing():
    source_result = run_sql_query_for_validation(f'''
        select distinct CustomerKey from DimCustomer
    ''')
    target_result = run_sql_query_for_validation(f'''
        select distinct CustomerKey from Dimcustomer_Target
    ''')

    # Extract the first element (index 0) from each row object
    source_keys = {row[0] for row in source_result}:wq






    target_keys = {row[0] for row in target_result}

    # Now the set comparison will work perfectly!
    assert source_keys == target_keys

#Transformation testing on any specific column
@pytest.mark.parametrize('Product_id',[
                        101,102,103,104
                         ])

def test_transformation_on_column(Product_id):
    source_query = run_sql_query_for_validation(f'''
      select CAST(Product_Price AS DECIMAL (18,2))* CAST(Quntity AS INT) from Product_Source where Product_id = {Product_id}
                       ''') [0][0]
    Target_query = run_sql_query_for_validation(f'''
     select CAST(Total_Price AS DECIMAL) from Product_Target where Product_id = {Product_id}
     ''')[0][0]

    assert  Target_query == source_query