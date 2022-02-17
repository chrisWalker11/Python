#must run with 2&> /dev/null to remove warning from python
import pandas as pd
df = pd.read_csv('amazon.csv')
df = df.fillna(0)
df["Item Subtotal"] = df["Item Subtotal"].str.replace('$','').astype(float)
total = df["Item Subtotal"].sum()
print(total)
