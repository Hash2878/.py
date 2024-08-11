import csv
num_attribute=6
a=[]
with open('enjoysport.csv','r') as file:
    reader=csv.reader(file)
    a=list(reader)
    hypothesis=a[1][:-1]
    for i in a:
        if i[-1] == 'yes':
            for j in range(num_attribute):
                if i[j]!=hypothesis[j]:
                    hypothesis[j]='?'

print("\n The maximally specific hypothesis for a given training examples:\n")
print(hypothesis)   
