from data import *
from functions import *
from config import *

old_column = sab_df.columns[0]
sab_df_new_column = sab_df.rename({sab_df.columns[0]: 'data'}, axis=1)

main_list = sab_df_new_column['data'].to_list()

new_df = {}
value_list = []
for i in main_list:
    i = iterate(first_filter, i, first_replacements)
    i = iterate(second_filter, i, second_replacements)
    i = iterate(third_filter, i, third_replacements)
    i = iterate(fourth_filter, i, fourth_replacements)
    value_list.append(i)
    new_df[old_column] = value_list

output_data(new_df)
