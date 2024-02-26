import os.path
from datetime import datetime
import pandas as pd
from data import *
import csv


def iterate(filters, iterator, dict_values):
    for one_filter in filters:
        if one_filter in iterator:
            for key, value in dict_values.items():
                iterator = iterator.replace(key, value)
    return iterator


def read_csv(path_name):
    python_list = []
    with open(path_name) as file:
        csv_file = csv.reader(file)
        for i in csv_file:
            python_list.extend(i)
    return python_list


def process(python_list):
    value_list = []
    for i in python_list:
        i = iterate(first_filter, i, first_replacements)
        i = iterate(second_filter, i, second_replacements)
        i = iterate(third_filter, i, third_replacements)
        i = iterate(fourth_filter, i, fourth_replacements)
        value_list.append(i)
    return value_list
def output_data(df,d):
    now = datetime.now()
    now = now.strftime('%Y-%m-%d %H:%M')
    output_path = os.path.join('output_dir',f'fyiz_file{d}_{now}.csv')
    pd.DataFrame(df).to_csv(output_path,index=False,header=False)