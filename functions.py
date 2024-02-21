from datetime import datetime
import pandas as pd


def iterate(filters, iterator, dict_values):
    for one_filter in filters:
        if one_filter in iterator:
            for key, value in dict_values.items():
                iterator = iterator.replace(key, value)
    return iterator


def output_data(df):
    now = datetime.now()
    now = now.strftime('%Y-%m-%d %H:%M')
    pd.DataFrame(df).to_csv(f'fyiz_file_{now}.csv',index=False)