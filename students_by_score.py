estudiantes=5  
record=[]
for i in range(estudiantes):
    name = "estudiante"+str(i)
    score = (i+1)*10
    student=[name,score]
    record.append(student)

record.sort(key = lambda student: (student[1],student[0]))
second_lowest= float('inf')
for student in record: 
    if student[1]==record[0][1]:
        continue
    if second_lowest>=student[1]:
        second_lowest=student[1]
        print(student[0])