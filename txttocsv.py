#importing necessary modules
import csv
import re

#introducing log file
filename = 'syslogsexample.txt'

dict1 = {}

fields =['datecom', 'time(ist)', 'ip']

#opening the log file
with open(filename) as fh:
    l = 1
    c = 0
    
    #segregating the key value pairs and storing them in dictionaries
    for line in fh:
        description = []
        description.append(line.split(' ', 2)[0]+" "+line.split(' ', 2)[1])
        description.append(line.split(' ', 3)[2])
        description.append(line.split(' ', 4)[3])
        match = re.finditer('\"\w+\s+(.*?)\"', line)
        for i in match:
            temp = i.group().replace(' ', '?#~')
            line = line.replace(str(i.group()), temp)
        description.extend(re.split(r'[ ""\n]', line[29:]))
        
        for i in description[:]:
            if fields[-1] != 'advpnsc':
                if '=' in i and i.index('=') == len(i)-1:
                    fields.append(i[:i.index('=')])
                    description.remove(i)
                elif '=' in i and i.index('=') != len(i)-1:
                    fields.append(i[:i.index('=')])
                    temp = i[i.index('=')+1:]
                    description[description.index(i)] = temp
            else:
                if '=' in i and i.index('=') == len(i)-1:
                    description.remove(i)
                elif '=' in i and i.index('=') != len(i)-1:
                    temp = i[i.index('=')+1:]
                    description[description.index(i)] = temp
            if i == '' or i == '\n':
                description.remove(i)
            if '?#~' in i:
                temp = i.replace('?#~', ' ')
                description[description.index(i)] = temp                                         
        
#making key value pairs        
        sno ='sys.log'+" "+str(l)
        i = 0
        dict2 = {}
        while i<len(fields):
            dict2[fields[i]]= description[i]
            i = i + 1
        dict1[sno]= dict2
        l = l + 1 
        list1 = []
        for i in range (1, l): 
            list1.append(dict1['sys.log '+str(i)])
        
print(list1)
        
#writing the csv file    
with open('dicttocsv.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=fields, lineterminator='\n')
    writer.writeheader()
    writer.writerows(list1)