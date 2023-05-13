import os
import pandas as pd
import json
basepath = '../sustainablefashion/'
ds = []
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.path)
            with open(entry.path, mode="r") as f:
                for line in f:
                    my_obj = json.loads(line)
                    ds.append(my_obj)

df = pd.DataFrame(ds)
df.to_csv ('../csv/sustainablefashion.csv', index=None)