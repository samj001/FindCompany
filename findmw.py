

import csv
import pandas as pd

w_file = open('w_business.csv','r')
all_file = open('all_business.csv','r')
w_reader = csv.reader(w_file)
all_reader = csv.reader(all_file)

all_dic = {}
for item in all_reader:
	if all_reader.line_num == 1:
		continue
	all_dic[item[0]] = item[1]

w_dic = {}
for item in w_reader:
	if w_reader.line_num == 1:
		continue
	w_dic[item[0].lower()] = [item[2],item[8]]


result = []
i=0
match = 0
for (key,value) in all_dic.items():
	
	if value.lower() in w_dic.keys():
		info = w_dic[value.lower()]
		dic = {'DOCid':key,'CompanyName':value,'IfMinorities/Women':'Y','ContactName':info[0],'Ethnicity':info[1]}
		match += 1
		
	else:
		dic = {'DOCid':key,'CompanyName':value,'IfMinorities/Women':'N','ContactName':None,'Ethnicity':None}

	result.append(dic)
	i += 1

print(i, ' companies searched')
print(match, ' companies matched')

columns = ['DOCid','CompanyName','IfMinorities/Women','ContactName','Ethnicity']
pd.DataFrame(result).to_csv('result.csv',index = False,columns = columns)

















