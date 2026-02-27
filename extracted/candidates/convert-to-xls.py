import json
import pandas as pd

with open("candidates-attachments-11.json", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

#transform the data to .xlsx format
df.to_excel("candidates-attachments-11.xlsx", index=False)