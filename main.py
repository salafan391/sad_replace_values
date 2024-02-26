from functions import process,output_data
from config import all_data


for count,proccess in enumerate(all_data):
    new_df = process(all_data[proccess])
    output_data(new_df,count)


