# complaint_list.py
import json, ssl, urllib.request
import time
import pandas as pd


FILE_PATH = "/data/files/complaint_list.csv"
API_URL = "https://datacenter.taichung.gov.tw/swagger/OpenData/37800d26-6574-4326-be6e-55c765b72f3d"


def call_complaint_list(url):
    context = ssl._create_unverified_context()
    with urllib.request.urlopen(url, context=context) as jsondata:
        data = json.loads(jsondata.read().decode("utf-8-sig"))
    csvs = []
    for i in data:
        if i["編號"]:
            csvs.append(i)
    df = pd.DataFrame(csvs)
    df.to_csv(FILE_PATH, index=False)
    json_str = json.dumps(csvs, ensure_ascii=False)
    print(json_str)


def main():
    call_complaint_list(API_URL)


if __name__ == "__main__":
    main()
