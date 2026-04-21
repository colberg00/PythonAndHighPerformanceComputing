import pandas as pd
import pyarrow as pa
import pyarrow.csv as pa_csv


def df_memsize(df):
    return df.memory_usage(deep=True).sum()


def reduce_dmi_df(df):
    df = df.copy()
    df['created'] = pd.to_datetime(df['created'])
    df['observed'] = pd.to_datetime(df['observed'])
    df['parameterId'] = df['parameterId'].astype('category')
    df['stationId'] = df['stationId'].astype('int16')
    df['value'] = df['value'].astype('float32')
    df['coordsx'] = df['coordsx'].astype('category')
    df['coordsy'] = df['coordsy'].astype('category')
    return df


def pyarrow_load(path):
    table = pa_csv.read_csv(path)
    return table.to_pandas()
