from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
# use a function to call and hold the dataset, you can call yours directly!
def get_data():
  db_url = f"mysql+pymysql://{os.getenv('db_username')}:{os.getenv('db_password')}@{os.getenv('db_host')}:{os.getenv('db_port')}/{os.getenv('db_database')}"
  engine = create_engine(db_url)
  query = 'select * from titanic_train'
  df = pd.read_sql(query, engine)
  return df




print(get_data)
print(get_data().head())