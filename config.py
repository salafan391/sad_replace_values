import os
from functions import read_csv



INPUT_DIR = 'input_dir'
path_names = []
for path in os.listdir(INPUT_DIR):
    path_names.append(os.path.join(INPUT_DIR, path))





all_data = {}
for num, path in enumerate(path_names):
    all_data[f"file{num}"] = read_csv(path)

