import pandas as pd
import numpy as np

def parse(file):
    data = open(r"data\processed\data1.csv", mode="w")
    with open(file) as f:
        lines = f.readlines()
        for k in range(len(lines)):
            line = lines[k]
            line = line.strip()
            if line.endswith(":"):
                movie_id = line.replace(":", "")
            else:
                row = [x for x in line.split(",")]
                row.insert(0, movie_id)
                data.write(",".join(row))
                data.write("\n")
file_path = r"data\netflix price data\combined_data_1.txt"
parse(file_path)
