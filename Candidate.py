import csv

with open('s.csv') as f:
    csv_file = csv.reader(f)
    data = list(csv_file)

s = data[1][:-1]
g = [['?' for _ in range(len(s))] for _ in range(len(s))]

for i in data:
    if i[-1] == 'yes':
        for j in range(len(s)):
            if i[j] != s[j]:
                s[j] = '?'
                g[j][j] = '?'
    elif i[-1] == 'no':
        for j in range(len(s)):
            if i[j] != s[j]:
                g[j][j] = s[j]
            else:
                g[j][j] = '?'

print("\nSteps of candidate elimination algorithm", data.index(i) + 1)
print(s)
print(g)

gh = []
for i in g:
    for j in i:
        if j != '?':
            gh.append(i)

print("\nFinal specific hypothesis:\n", s)
print("\nFinal general hypothesis:\n", gh)
