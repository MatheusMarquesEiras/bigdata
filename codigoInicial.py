import pandas as pd
data = pd.read_csv('ner_dataset.csv', encoding= 'unicode_escape')
print(data.head(10))