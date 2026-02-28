import json
import pandas as pd

with open("notes-candidate-very-important-attachments-1.json", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

#transform the data to .xlsx format
df.to_excel("notes-candidate-very-important-attachments-1.xlsx", index=False)