from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os

def save_predictions(df, table_name='titanic_with_predictions'):
    db_url = f"mysql+pymysql://{os.getenv('db_username')}:{os.getenv('db_password')}@{os.getenv('db_host')}:{os.getenv('db_port')}/{os.getenv('db_database')}"
    engine = create_engine(db_url)
    df.to_sql(table_name, con=engine, index=False, if_exists='replace')
    print(f"✅ Predictions saved to table: `{table_name}` in your database!")