
import csv

with open('enjoysport.csv','r') as f:
    csv_file=csv.reader(f)
    data=list(csv_file)
    specific=data[1][:-1]
    general=[['?'for i in range(len(specific))] for j in range(len(specific))]
    for i in data:
        if i[-1]=="yes":
            for j in range(len(specific)):
                if i[j]!=specific[j]:
                    specific[j]="?"
                    general[j][j]="?"
        elif i[-1]=="no":
            for j in range(len(specific)):
                if i[j]!=specific[j]:
                    general[j][j]=specific[j]
                else:
                    general[j][j]="?"
        print("\nstep "+str(data.index(i)+1)+" of candidate elimination algorithm")
        print(specific)
        print(general)
    gh=[]# gh=general hypothesis
    for i in general:
        for j in i:
            if j!='?':
                gh.append(i)
                break
    print("\nFinal specific hypothesis:\n",specific) 
    print("\nFinal general hypothesis:\n",gh)          
