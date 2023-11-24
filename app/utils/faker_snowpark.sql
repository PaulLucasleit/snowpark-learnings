/*
With the introduction of Snowpark on Snowflake, we can now use Python libraries to generate dummy data and populate tables in Snowflake. 
This can be useful for demonstrating tools and functions within Snowflake.

We can use the Python library Faker to generate data, and Pandas to structure the data in a DataFrame, to load into a table.
*/

-- First check that the library you are hoping to use exists.
SELECT * 
FROM information_schema.packages 
WHERE language = 'python' AND package_name ilike '%faker%';

-- Now we know Faker exists, we can use a Python UDF to generate fake data.
-- In this example, we are creating 10 rows, for ID, name, and date.
-- To alter the number of rows produced, edit the parameter when calling the function.
CREATE OR REPLACE PROCEDURE GENERATE_FAKE_DATA_DEMO(NUM_ROWS INTEGER)
RETURNS VARCHAR
LANGUAGE PYTHON
RUNTIME_VERSION = '3.10'
PACKAGES = ('snowflake-snowpark-python', 'faker')
HANDLER = 'generate_data'
AS
$$
def generate_data(session, NUM_ROWS):
    import faker
    fake = faker.Faker()
    data_str = fake.csv(
        data_columns=(
            '{{name}}', 
            '{{date}}'), 
            num_rows=NUM_ROWS, 
            include_row_ids=True
        ).replace('"', '')
    return(data_str)
$$;

CALL GENERATE_FAKE_DATA_DEMO(10);

-- Now we have a single output of data, we can use Pandas to turn the data into a DataFrame, and load into a Snowflake table.
-- In this example, we are updating the previous UDF above to add this additional functionality.
-- When calling the function, pass in the number of rows, and table name to be created.
USE DATABASE SNOWPARK_DEMO;
USE SCHEMA DBO;

CREATE OR REPLACE PROCEDURE GENERATE_FAKE_DATA_DEMO(NUM_ROWS INTEGER, TABLE_NAME VARCHAR)
RETURNS VARCHAR
LANGUAGE PYTHON
RUNTIME_VERSION = '3.10'
PACKAGES = ('snowflake-snowpark-python', 'faker')
HANDLER = 'generate_data'
AS
$$
def generate_data(session, NUM_ROWS, TABLE_NAME):
    import faker
    from snowflake.snowpark.types import IntegerType, StringType, DateType, StructType, StructField
    
    fake = faker.Faker()
    data_str = fake.csv(
        data_columns=(
            '{{name}}', 
            '{{date}}'), 
            num_rows=NUM_ROWS, 
            include_row_ids=True
        ).replace('"', '')
        
    schema_for_demo = StructType(
        [
            StructField("ID", IntegerType(), False),
            StructField("Name", StringType(), False),
            StructField("Date", DateType(), False)
        ]
    )

    df = session.create_dataframe([x.split(',') for x in data_str.split('\r\n')[0:-1]], schema_for_demo)
    df.write.mode("overwrite").save_as_table(TABLE_NAME)
    return('Success')
$$;

CALL GENERATE_FAKE_DATA_DEMO(10, 'SNOWPARK_DEMO_TABLE');

SELECT * FROM SNOWPARK_DEMO.DBO.SNOWPARK_DEMO_TABLE;
