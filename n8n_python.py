# n8n_python.py - Python code in the node "Code" of n8n
import json
import pandas as pd


def top10_in_etfs(j_str):
    dic = json.loads(j_str)
    etfs = []
    for etf in dic["etf_data"]:
        for content in etf["etf_holding"]:
            etfs.append(content)
    df = pd.DataFrame(etfs)
    cols_group = ["s_code", "s_name"]
    col_sum = "holding_amount"
    df_amt = df.groupby(cols_group)[col_sum].sum().reset_index()
    df_amt_ranking = df_amt.sort_values(col_sum, ascending=False)
    dic = df_amt_ranking.head(10).to_dict(orient="records")
    return dic


# Get the results of previous node in n8n
j_str = _input.first().json.stdout

ds = top10_in_etfs(j_str)

# Pass data to next node in n8n
return ds