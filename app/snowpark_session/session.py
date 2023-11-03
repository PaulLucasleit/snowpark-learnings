from snowflake.snowpark.session import Session
from snowflake.snowpark.types import LongType

from app.settings.settings import SNOWFLAKE_CONNECTION_PARAMS


def snowpark_session():
    return Session.builder.configs(SNOWFLAKE_CONNECTION_PARAMS).create()
