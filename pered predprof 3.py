#3
fin=open('students.csv', 'r', encoding='utf-8')
title=fin.readline()
students=[x.strip().split(',') for x in fin]
fin.close()
while True:
    a=input()
    if a=='СТОП':
        break
    else:
        for x in students:
            if x[2]==a:
                fio=x[1].split()
                flag=False
                print(f'Проект № {x[2]} делал(а): {fio[0][1]}.{fio[0]} он(а) получил(а) оценку - {x[4]}')
                break
        else:
            print('Ничего не найдено')









                
