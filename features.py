import pandas as pd
from db_pull import get_data

df = get_data()


def lenght_name(df):
  df = df.copy()
  if 'name' in df.columns:
    df['lenght_of_name'] = df['Name'].apply(len)
  return df


def is_a_minor(df):
  df = df.copy()
  df['is_a_minor'] = df['Age'].apply(lambda x: 1 if x < 18 else 0)
  return df


def add_features(df):
  df = lenght_name(df)
  df = is_a_minor(df)

  return df

df_temp = df.copy()

df_temp = add_features(df_temp)

print(df_temp.head())
