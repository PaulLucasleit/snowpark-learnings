from snowflake.snowpark.session import Session

from app.settings.settings import SNOWFLAKE_CONNECTION_PARAMS


def snowpark_session():
    return Session.builder.configs(SNOWFLAKE_CONNECTION_PARAMS).create()
