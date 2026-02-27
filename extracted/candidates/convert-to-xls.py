import json
import pandas as pd

with open("candidates-9.json", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

#transform the data to .xlsx format
df.to_excel("candidates-9.xlsx", index=False)