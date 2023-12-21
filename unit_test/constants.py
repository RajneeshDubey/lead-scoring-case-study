# You can create more variables according to your project. The following are the basic variables that have been provided to you
DB_PATH = '/home/Assignment/01_data_pipeline/scripts/'
DB_FILE_NAME = 'utils_output.db'
TEST_DB_FILE_NAME = 'unit_test_cases.db'
DATA_DIRECTORY = '/home/Assignment/01_data_pipeline/scripts/leadscoring_test.csv'
INTERACTION_MAPPING = '/home/Assignment/01_data_pipeline/scripts/interaction_mapping.csv'
INDEX_COLUMNS_TRAINING = ['created_date', 'city_tier', 'first_platform_c',
       'first_utm_medium_c', 'first_utm_source_c', 'total_leads_droppped',
       'referred_lead', 'app_complete_flag']
INDEX_COLUMNS_INFERENCE = []
NOT_FEATURES = ['created_date', 'assistance_interaction', 'career_interaction',
                'payment_interaction', 'social_interaction', 'syllabus_interaction']
CITY_TIER_MAPPING = 'city_tier_mapping'
ORIGINAL_DATA = "loaded_data"
CITY_TIER_MAPPED = "city_tier_mapped"
CATAEGORICAL_VALUES_MAPPED = "categorical_variables_mapped"
INTERACTIONS_MAPPED = "interactions_mapped"