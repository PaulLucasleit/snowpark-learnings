from pathlib import Path
import os

import dotenv


def env_var(var, default=None):
    """Gets environment variable. Return default if not present, or if present but empty."""
    return os.environ.get(var, default) or default


dotenv.load_dotenv()

PROJECT_ROOT = Path(__file__).parent.parent
TEMP_ROOT = PROJECT_ROOT / ".temp"
# Make the temp directory if it doesn't exist
TEMP_ROOT.mkdir(parents=True, exist_ok=True)


# Snowflake
SNOWFLAKE_ACCOUNT = env_var("SNOWFLAKE_ACCOUNT")
SNOWFLAKE_USER = env_var("SNOWFLAKE_USER")
SNOWFLAKE_PASSWORD = env_var("SNOWFLAKE_PASSWORD")
SNOWFLAKE_ROLE = env_var("SNOWFLAKE_ROLE")
SNOWFLAKE_WAREHOUSE = env_var("SNOWFLAKE_WAREHOUSE")
SNOWFLAKE_DATABASE = env_var("SNOWFLAKE_DATABASE")
SNOWFLAKE_SCHEMA = env_var("SNOWFLAKE_SCHEMA")

SNOWFLAKE_CONNECTION_PARAMS = dict(
    account=SNOWFLAKE_ACCOUNT,
    user=SNOWFLAKE_USER,
    password=SNOWFLAKE_PASSWORD,
    role=SNOWFLAKE_ROLE,
    warehouse=SNOWFLAKE_WAREHOUSE,
    database=SNOWFLAKE_DATABASE,
    schema=SNOWFLAKE_SCHEMA,
)