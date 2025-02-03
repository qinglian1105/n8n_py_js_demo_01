# n8n_python.py
import pandas as pd
import json


def processing_data(jstr):
    int_cols = ["編號", "件數"]
    float_cols = ["該業務占排名前十大百分比"]
    dic = json.loads(jstr)
    df = pd.DataFrame(dic)
    df[int_cols] = df[int_cols].astype(int)
    df[float_cols[0]] = df[float_cols[0]].str.replace("%", "").astype(float)
    ds = df.to_dict(orient="records")
    return ds


# Get the results of previous node in n8n 
jstr = _input.first().json.stdout

ds = processing_data(jstr)

# Pass data to next node in n8n
return ds
