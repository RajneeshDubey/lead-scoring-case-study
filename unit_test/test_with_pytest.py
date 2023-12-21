##############################################################################
# Import the necessary modules
# #############################################################################

from constants import *
import utils
import pandas as pd
import os
import sqlite3
from sqlite3 import Error

###############################################################################
# Write test cases for load_data_into_db() function
# ##############################################################################

def test_load_data_into_db():
    """_summary_
    This function checks if the load_data_into_db function is working properly by
    comparing its output with test cases provided in the db in a table named
    'loaded_data_test_case'

    INPUTS
        DB_FILE_NAME : Name of the database file 'utils_output.db'
        DB_PATH : path where the db file should be present
        UNIT_TEST_DB_FILE_NAME: Name of the test database file 'unit_test_cases.db'

    SAMPLE USAGE
        output=test_get_data()

    """
    conn = sqlite3.connect(DB_PATH+DB_FILE_NAME)
    loaded_data = pd.read_sql("select * from "+ORIGINAL_DATA,conn)
    
    conx = sqlite3.connect(TEST_DB_FILE_NAME)
    test_data = pd.read_sql("select * from loaded_data_test_case",conx)

    conn.close()
    conx.close()
    
    cl1=set(loaded_data.columns)
    cl2=set(test_data.columns)
    cl3=set()

    if( (cl1.difference(cl2)==cl3) and  (cl2.difference(cl1)==cl3) ):
         print("loaded_data_test_case")
    assert (cl1.difference(cl2)==cl3) and  (cl2.difference(cl1)==cl3)
    

###############################################################################
# Write test cases for map_city_tier() function
# ##############################################################################
def test_map_city_tier():
    """_summary_
    This function checks if map_city_tier function is working properly by
    comparing its output with test cases provided in the db in a table named
    'city_tier_mapped_test_case'

    INPUTS
        DB_FILE_NAME : Name of the database file 'utils_output.db'
        DB_PATH : path where the db file should be present
        UNIT_TEST_DB_FILE_NAME: Name of the test database file 'unit_test_cases.db'

    SAMPLE USAGE
        output=test_map_city_tier()

    """
    conn = sqlite3.connect(DB_PATH+DB_FILE_NAME)
    city_mapped_data = pd.read_sql("select * from city_tier_mapped",conn)
    
    conx = sqlite3.connect(TEST_DB_FILE_NAME)
    test_data = pd.read_sql("select * from city_tier_mapped_test_case",conx)
    conn.close()
    conx.close()
    
    cl1=set(city_mapped_data.columns)
    cl2=set(test_data.columns)
    cl3=set()
    
    if( (cl1.difference(cl2)==cl3) and  (cl2.difference(cl1)==cl3) ):
         print("city_tier_mapped_test_case")
    assert (cl1.difference(cl2)==cl3) and  (cl2.difference(cl1)==cl3)

    

###############################################################################
# Write test cases for map_categorical_vars() function
# ##############################################################################    
def test_map_categorical_vars():
    """_summary_
    This function checks if map_cat_vars function is working properly by
    comparing its output with test cases provided in the db in a table named
    'categorical_variables_mapped_test_case'

    INPUTS
        DB_FILE_NAME : Name of the database file 'utils_output.db'
        DB_PATH : path where the db file should be present
        UNIT_TEST_DB_FILE_NAME: Name of the test database file 'unit_test_cases.db'
    
    SAMPLE USAGE
        output=test_map_cat_vars()

    """
    conn = sqlite3.connect(DB_PATH+DB_FILE_NAME)
    categorical_mapped_data = pd.read_sql("select * from "+CATAEGORICAL_VALUES_MAPPED,conn)
    
    conx = sqlite3.connect(TEST_DB_FILE_NAME)
    test_data = pd.read_sql("select * from categorical_variables_mapped_test_case",conx)
    
    conn.close()
    conx.close()
    
    cl1=set(categorical_mapped_data.columns)
    cl2=set(test_data.columns)
    cl3=set()
    
    if( (cl1.difference(cl2)==cl3) and  (cl2.difference(cl1)==cl3) ):
         print("categorical_variables_mapped_test_case")
    assert (cl1.difference(cl2)==cl3) and  (cl2.difference(cl1)==cl3)
    

###############################################################################
# Write test cases for interactions_mapping() function
# ##############################################################################    
def test_interactions_mapping():
    """_summary_
    This function checks if test_column_mapping function is working properly by
    comparing its output with test cases provided in the db in a table named
    'interactions_mapped_test_case'

    INPUTS
        DB_FILE_NAME : Name of the database file 'utils_output.db'
        DB_PATH : path where the db file should be present
        UNIT_TEST_DB_FILE_NAME: Name of the test database file 'unit_test_cases.db'

    SAMPLE USAGE
        output=test_column_mapping()

    """ 
    conn = sqlite3.connect(DB_PATH+DB_FILE_NAME)
    interactions_mapped_data = pd.read_sql("select * from "+INTERACTIONS_MAPPED,conn)
    
    conx = sqlite3.connect(TEST_DB_FILE_NAME)
    test_data = pd.read_sql("select * from interactions_mapped_test_case",conx)
    
    conn.close()
    conx.close()
    
    cl1=set(interactions_mapped_data.columns)
    cl2=set(test_data.columns)
    cl3=set()
    
    if( (cl1.difference(cl2)==cl3) and  (cl2.difference(cl1)==cl3) ):
         print("interactions_mapped_test_case")
    assert (cl1.difference(cl2)==cl3) and  (cl2.difference(cl1)==cl3)
   

if __name__ == "__main__":
    test_load_data_into_db()
    test_map_city_tier()
    test_map_categorical_vars()
    test_interactions_mapping()
    print("Everything passed")