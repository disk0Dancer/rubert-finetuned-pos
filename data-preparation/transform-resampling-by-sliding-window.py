import json
from collections import Counter
import numpy as np
import pandas as pd
from copy import deepcopy

with open('data.json', 'r', encoding="utf-8") as f:
    data = json.loads(f.read())

TEST_N = 40
df_data = pd.DataFrame(data).T
df_data.iloc[-TEST_N:-TEST_N//2].to_csv('data-resampled-val.csv', index=False, sep="\t")
df_data.iloc[-TEST_N//2:].to_csv('data-resampled-test.csv', index=False, sep="\t")
print(df_data.head())


all_tags = ' '.join(v['schema'] for k, v in data.items())
print('\n\n\n----------before-sampling-----------')
print("Всего наблюдений:", 100-TEST_N)
print("Всего тегов:", len(all_tags.split()))
print("Уникальных тегов:", len(set(all_tags.split())))
print("counter:", Counter(all_tags.split()))

sents = [v['schema'] for k, v in data.items()]
sents_len = [len(s) for s in sents]
print("\nДлинна предложений\nmin", min(sents_len))
print("max", max(sents_len))
print("avg", np.average(sents_len))


sampled = {}
j = 100
for i in range(100-TEST_N):
    sent = data[f'{i}']
    ru = sent['ru'].split()
    schema = sent['schema'].split()
    n = len(sent['schema'].split())

    for window in range(1, n):
        for left in range(0, n):
            right = left + window # [left : right)
            if right >= n:
                break

            sampled[f"{j}"] = {
                'ru': ' '.join(ru[left: right]),
                'schema': ' '.join(schema[left: right]),
                }
            j += 1

all_tags = ' '.join(v['schema'] for k, v in sampled.items())
print('\n\n\n----------post-sampling-----------')
print("Всего наблюдений:", max(int(i) for i in sampled.keys()))
print("Всего тегов:", len(all_tags.split()))
print("counter:", Counter(all_tags.split()))

sents = [v['schema'] for k, v in sampled.items()]
sents_len = [len(s) for s in sents]
print("\nДлинна предложений\nmin", min(sents_len))
print("max", max(sents_len))
print("avg", np.average(sents_len), '\n')

df = pd.DataFrame(sampled).T
df.to_csv('data-resampled-train.csv', index=False, sep='\t')
