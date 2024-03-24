import json
import pandas as pd
from string import punctuation as punct

punct = set(punct + '…' + '»' + '«')
# TODO : note: @Adv/action time -> @Adv/action_time


with open("/Users/admin/Desktop/research/code/data.txt", 'r', encoding="utf-8-sig") as f:
    data = f.read()

data_iter = filter(lambda x: len(x)>0, data.split('\n'))
russian, schema, current_schema = [], [], {}

for line in data_iter:
    if len(line) == 0:
        continue

    if line.split()[0][-1]=='.' and line[0]!='@':
        schema.append(current_schema)
        current_schema = {}
        ru = ' '.join(line.split()[1:]).replace('...', '…')
        res = ''
        for i in range(len(ru)-1):

            if ru[i] in punct:
                if ru[i+1] in punct:
                    res += ru[i] + " "
                elif ru[i+1]==' ':
                    res += ru[i]
                else:
                    if ru[i]=='-':
                        res += ru[i]
                    else:
                        res += ru[i] + " "

            elif ru[i+1] in punct:
                if ru[i+1]=='-':
                    res += ru[i]
                else:
                    res += ru[i] + " "
            else:
                res += ru[i]

        russian.append(res+ru[-1])


    elif line[0]=='@':
        # TODO modify key if needed
        current_schema[line[1:].replace('\t', '')] = list(map(int, next(data_iter).split(', ')))
        

schema.append(current_schema)
schema = schema[1:]

tags_schema = []
for i in range(100):
    sent = []
    for k, v in schema[i].items():
        for pos in v:
            sent.append((pos, k))
    sent.sort(key=lambda x: x[0])
    tags_schema.append(' '.join(f"{x[1]}" for x in sent))

c = 0
data = {}
for i, ru, tags in zip(range(100), russian, tags_schema):
    data[i] = {
        "ru": ru,
        "schema": tags,
    }
    if len(ru.split()) == len(tags.split()):
        c+=1
    else:
        print("assert lens")
        break

print(c/len(data))
    
with open('data.json', 'w', encoding="utf-8") as f:
    f.write(json.dumps(data, indent=4))

with open('data.json', 'r', encoding="utf-8") as f:
    print(json.loads(f.read())['99'])


with open('data.json', 'r', encoding="utf-8") as f:
    data = json.loads(f.read())


TEST_N = 40
df_data = pd.DataFrame(data).T
df_data.iloc[:-TEST_N].to_csv('data-original-train.csv', index=False, sep="\t")
df_data.iloc[-TEST_N:-TEST_N//2].to_csv('data-original-val.csv', index=False, sep="\t")
df_data.iloc[-TEST_N//2:].to_csv('data-original-test.csv', index=False, sep="\t")
print(df_data.head())