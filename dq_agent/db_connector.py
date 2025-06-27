
from sqlalchemy import create_engine
import pandas as pd

def connect_db(db_type, username, password, host, port, dbname):
    """Create a SQLAlchemy engine based on database credentials."""
    db_uri = f"{db_type}://{username}:{password}@{host}:{port}/{dbname}"
    engine = create_engine(db_uri)
    return engine

def read_table(engine, table_name):
    """Read a table into a pandas DataFrame."""
    return pd.read_sql(f"SELECT * FROM {table_name}", engine)

def write_table(df, engine, table_name, if_exists="replace"):
    """Write a DataFrame back to a table."""
    df.to_sql(table_name, engine, index=False, if_exists=if_exists)
