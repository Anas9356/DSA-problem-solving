class student:
    name=""
    age=0
    location =""
n = int(input())
studList=[]
for i in range(n):
    currStud = student()
    currStud.name= input()
    currStud.age = int(input())
    currStud.location=input()
    studList.append(currStud)
for i in range(n):
    print(studList[i].name)