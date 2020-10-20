import pandas as pd
df = pd.read_json (r'tabulas.json')
df.to_csv (r'tabulas.csv', index = None)
