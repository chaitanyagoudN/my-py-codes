# Using readlines()
file1 = open("C:\\Users\\CHAITANYA\\OneDrive\\Desktop\\628\\gradesFile.txt", 'r')
Lines = file1.readlines()
  
count = 0
arr=[]
for line in Lines:
    subLine=line.split("\t")
    subarry=[]
    for sline in subLine:
        if sline=="" or sline=='' or sline=='\n':
            subarry.append(0)
        elif '\n' in sline:
            subarry.append(int(sline[0:len(sline)-1]))
        else:
            subarry.append(int(sline))
    arr.append(subarry)


print(arr)

#1:
for sub in arr:
    print("No of asignments:", len(sub)-1)
    break

#2:
points=0
cnt=0
for sub in arr:
    for isub in sub:
        if cnt==0:
            cnt=cnt+1
            continue
        else:
            points=points+int(isub)
    break
print("Total no of availabe points :",points)


#3:
students=0
counter=0
for sub in arr:
    if counter==0:
        counter=counter+1
        continue
    else:
        students=students+1
print("Total number of students :",students)


#4:
total=0
higest={}
higest_result={}
student_id=0
arrcount=0
tmp1=0
prevstudent=0
marks=0
for sub in arr:
    if arrcount==0:
        arrcount=arrcount+1
        continue
    else:
        points=0
        c=0
        for isub in sub:
            if c==0:
                c=c+1
                student_id=int(isub)
                continue
            else:
                points=points+int(isub)
    higest[student_id]=points

result=0
id=0
for key in higest:
    if higest[key]>result:
        result=higest[key]
        id=key
    else:
        continue
higest_result[id]=result

print("Highest graded students :",higest_result)


#5:
total=0
lowest={}
lowest_result={}
student_id=0
arrcount=0
tmp1=0
prevstudent=0
marks=0
for sub in arr:
    if arrcount==0:
        arrcount=arrcount+1
        continue
    else:
        points=0
        c=0
        for isub in sub:
            if c==0:
                c=c+1
                student_id=int(isub)
                continue
            else:
                points=points+int(isub)
    lowest[student_id]=points

result=0
id=0
for key in lowest:
    if result>lowest[key] or result==0:
        result=lowest[key]
        id=key
    else:
        continue
lowest_result[id]=result

print("Lowest graded students :",lowest_result)

#6:
missingStudents=set()
student_id=0
x=0
for sub in arr:
    if x==0:
        x=x+1
        continue
    else:
        c=0
        for isub in sub:
            if c==0:
                c=c+1
                student_id=int(isub)
                continue
            else:
                if isub==0:
                    missingStudents.add(student_id)
print("students with missings grades :",missingStudents)
