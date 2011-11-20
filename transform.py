import csv

r = csv.reader(open('training.csv'))
rows = [x for x in r]
rows = rows[1:35000]

words = set()
for row in rows:
    for x in [6, 7, 8]:
        ws = row[x].split(' ')
        [words.add(w) for w in ws]
words = list(words)
words.sort()

new_rows = []
new_rows.append(['lat', 'long', 'qual'] + words + ['good'])
new_rows.append(['c', 'c', 'c'] + (['d'] * len(words)) + ['d'])
new_rows.append(['', '', ''] + ([''] * len(words)) + ['class'])

for row in rows:
    new_row = []
    new_row.append(row[1])
    new_row.append(row[2])
    if row[4] != '0' and row[3] != '0':
        new_row.append(float(row[5])/(float(row[4])*float(row[3])))
    else:
        new_row.append('')
    for w in words:
        if w in row[6] or w in row[7] or w in row[8]:
            new_row.append(1)
        else:
            new_row.append(0)
    new_row.append(row[9])
    new_rows.append(new_row)
    
with open('training.tab', 'w') as f:
    w = csv.writer(f, delimiter='\t')
    w.writerows(new_rows)

# jklfds
# 
# import csv
# r = csv.reader(open('test.csv'))
# rows = [x for x in r][1:]
# ids = [r[0] for r in rows]
# 
# def b_dev(a, p):
#     from math import log
#     if p > 0.99:
#         p = 0.99
#     if p < 0.01:
#         p = 0.01
#     return -(a * log(p, 10) + (1 - a) * log((1-p), 10))
#     
# [b_dev(int(d.getclass().value), forest(d, orange.GetProbabilities)[1]) for d in test_data]