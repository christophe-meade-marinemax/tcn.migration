import json
import pandas as pd

with open("candidates-attachments-10.json", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

#transform the data to .xlsx format
df.to_excel("candidates-attachments-10.xlsx", index=False)