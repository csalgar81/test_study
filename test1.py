"""
file_1 = open('grades.txt','r')
content = file_1.read()
content += '\nwomen,9.5'
file_1.close()
file_2 = open('grades.txt','w')
print(content,file = file_2 )
"""

file_3 = open('grades.txt','r')
content = file_3.readlines()
list_1 =[]
for item in content:
     list_1.append(item.split(','))
print(list_1)


# list_2 = [item.split()for item in content]
# print(list_2)

sum = 0
for item in list_1:
    print(item[0],'\t', item[1])
    sum += float(item[1])
print(sum)

