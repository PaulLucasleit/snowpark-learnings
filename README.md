# snowpark-learnings

### Setup

1. Install libraries by running `pip install -r requirements.txt` in root of repo
2. Copy `.env-example` as `.env` and fill in Snowflake details
3. In root of directory in terminal, run `jupyter notebook`. This will open a new browser window for jupyter notebooks

### Notebooks
The notebooks can be found in `app/notebooks/`

If you want to create a new notebook, duplicate/copy the `template.ipynb`, which has minimal imports required for snowpark


### Snowflake Sample Data

The examples I use depend on the Snowflake sample data. If you haven't got this already
you can get the data share by running the following in your snowflake instance

```sql
-- Create a database from the share.
CREATE DATABASE SNOWFLAKE_SAMPLE_DATA FROM SHARE SFC_SAMPLES.SAMPLE_DATA;

-- Grant the PUBLIC role access to the database.
-- Optionally change the role name to restrict access to a subset of users.
GRANT IMPORTED PRIVILEGES ON DATABASE SNOWFLAKE_SAMPLE_DATA TO ROLE PUBLIC;
```

More details on the Snowflake sample data can be found [here](https://docs.snowflake.com/en/user-guide/sample-data-using)


### Examples Followed

1. Follow along with youtube vids  
   [Snowpark For Python | Snowflake Tutorial](https://youtu.be/udcFnIvXFnE)  
   [Intermediate Data Transformations in Snowpark for Python | Snowflake Tutorial](https://youtu.be/kKOMXL6U3AE)  
   [Advanced Data Transformations in Snowpark for Python | Snowflake Tutorial](https://youtu.be/WVUo_NCWclg)


2. Snowflake Demo -  
   [Machine Learning with Snowpark Python](https://quickstarts.snowflake.com/guide/getting_started_snowpark_machine_learning/?index=..%2F..index#0)


### Useful Resources

* [Better Practices with Snowpark](https://medium.com/snowflake/lets-talk-about-some-better-practices-with-snowpark-python-python-udfs-and-stored-procs-903314944402)