class student:
    def __init__(self, studentid, studentname, studentclass, fee, feepaid):
        self.studentid = studentid
        self.studentname = studentname
        self.studentclass = studentclass
        self.fee = fee
        self.feepaid = feepaid
    
class school:
    def __init__(self, buslist, studentlist):
        self.buslist = buslist
        self.studentlist = studentlist

    def getFeeForStudentUsingBus(self):

        if len(buslist)==0 or len(studentlist)==0: return None

        dictionary={}
        for i in studentlist:
            if i.studentid in buslist:
                dictionary[i.studentid]=i.fee+1200
        
        return dictionary

    def getFeeForStudentUsingStudent(self, string):
        listofstudents=[]
        for i in studentlist:
            clastu = i.studentclass.split("-")[0]
            if i.feepaid.lower() =="no" and clastu ==string:
                listofstudents.append(i)

        #sort studentlist according to name
        listofstudents.sort(key=lambda x: x.studentname)
        return listofstudents
                

n = int(input())
studentlist=[]
while n: 
    studentid= int(input())
    studentname = input()
    studentclass = input()
    fee = int(input())
    feepaid = input()
    studentlist.append(student(studentid, studentname, studentclass, fee, feepaid))
    n-=1
buslist=[]
m = int(input())
while m:
    buslist.append(int(input()))
    m-=1

string=input()

s=school(buslist, studentlist)
dictbus = s.getFeeForStudentUsingBus()
liststudent = s.getFeeForStudentUsingStudent(string)

if dictbus:
    for i in dictbus:
        print(i,dictbus[i],sep="#")
else:
    print("no student availed bus service")

if liststudent:
    for i in liststudent:
        print(i.studentid, i.studentname, i.studentclass, sep="#")
else:
    print("class not present or all fee paid")

'''
5
101
aparna
III-A
1200
no
102
kiran
II-B
1800
yes
103
raman
IV-A
1800
no
104
rishab
IV-B
2000
yes
105
minu
V-C
2100
no
0
1

5
101
Aradhana
II-A
1200
yes
102
Jyoti
III-B
1800
yes
103
Prakash
III-A
1800
no
104
Harsh
IV-B
2000
yes
105
Kriti
III-C
1800
No
3
101
103
104
III
'''