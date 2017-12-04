import csv
import re #remove white spaces

f=open("final.csv")
outputFile=open("new_final.csv",'w')

wspace=[]

morethan7=[]

result=[]

csv_f=csv.reader(f)


for row in csv_f:
    d=re.sub(' ','',row[1])
    wspace.append(d)

for i in wspace:
    l=len(i)
    if l<10:
        diff=10-l
        if diff<7:
            morethan7.append(i)
        x=diff
        y=""
        for j in range(x):
            y = y + "0"

        i= str(i)
        b=y+i
        result.append(b)
    else:
        result.append(str(i))
        
#print result

for row in result:
    outputFile.write(row+"\n")

outputFile.close()
f.close()