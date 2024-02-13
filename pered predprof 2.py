#2
fin=open('students.csv', 'r', encoding='utf-8')
title=fin.readline()
students=[x.strip().split(',') for x in fin]
fin.close()

for i in range(len(students)):
    for j in range(i, 0, -1):
        if students[j][4]<students[j-1][4]:
            students[j], students[j-1] = students[j-1], students[j]
cnt=1
print('10 класс')
for i in range(len(students)):
    if students[i][3][:2]=='10' and students[i][4]=='5':
        fio=students[i][1].split()
        print(f'{cnt} место: {fio[1][0]}.{fio[0]}')
        cnt+=1
    if cnt==4:
        break
