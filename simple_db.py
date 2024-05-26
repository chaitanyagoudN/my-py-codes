import requests
import json

class Department:
    def __init__(self, title, code, phone):
        self.title = title
        self.phone = phone
        self.code = code
        

academicTerms = "https://courseregistration.apps.cmich.edu/api/Services/AcademicTermsInfo"
departmentBase = "https://courseregistration.apps.cmich.edu/api/Services/Departments/"
searchBase = "https://courseregistration.apps.cmich.edu/api/Services/Search"

acad_list=[]
Value=-1
academicTerm = ""
department = "_EMPTY_"
genEd = "_EMPTY_"
location = "_EMPTY_"
keyword = "_EMPTY_"


acad_search=f"{academicTerms}"
r = requests.get(acad_search)
results = json.loads(r.text)
acadedict={}

for result in results:
    acad_list.append(result['academicSession']['displayText'])
    acadedict[result['academicSession']['displayText']]=result['academicSession']['value']
    Value=Value+1


AcademicInput=int(input("0 - Summer 2022\n1 - Fall 2022\n2 - Spring 2023\n select academic term :"))
mnthYear=acadedict[acad_list[AcademicInput]]

r = requests.get(departmentBase + mnthYear[0:4]+"/"+mnthYear[4:])
results = json.loads(r.text)
for result in results:
    dept = Department(result["title"], result["departmentCode"], result["phone"])
    print("Depatment Title -",dept.title,"---------", "department Code -",result["departmentCode"],)

option= int(input("1 -Last Name\n2 - course_code\n3 - department\nEnter valid detail :"))
if option==1:
    keyword=input("Give Lastname: ")
    searchUrl = f"{searchBase}/{mnthYear}/{department}/{genEd}/{location}/{keyword}"
elif option==2:
    genEd=input("Give course code: ")
    searchUrl = f"{searchBase}/{mnthYear}/{department}/{location}/{keyword}/{genEd}"
elif option==3:
    department=input("Give department code: ")
    searchUrl = f"{searchBase}/{mnthYear}/{department}/{genEd}/{location}"
else:
    print("choose valid option only")

print(searchUrl)
r = requests.get(searchUrl)
results = json.loads(r.text)
print(results)