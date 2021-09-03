class Leave:
    def __init__(self, leaveId, leaveType, noOfDays, dateOfApplication):
        self.leaveId = leaveId
        self.leaveType = leaveType
        self.noOfDays = noOfDays
        self.dateOfApplication = dateOfApplication
        
class Employee:
    def __init__(self , leaveList, leaveBalance):        
        self.leaveList = leaveList
        self.leaveBalance = leaveBalance
        
    def getUpdatedLeaveBalance(self):
        for i in leaveList:
            leavetype = i.leaveType
            leaveday = i.noOfDays
            
            if i.leaveType in leaveBalance and leaveday<=leaveBalance[i.leaveType]:
                leaveBalance[leavetype] = leaveBalance[leavetype] - leaveday
            else:
                print("Insufficient balance for " + i.leaveType + " applied on "+ i.dateOfApplication)
                
        for i in sorted(leaveBalance):
            print( i , str(leaveBalance[i]), sep=":")
            
    def getLeaveCount(self,startmonth,endmonth):
        count = 0
        for i in self.leaveList:
            month = int(i.dateOfApplication.split("-")[1])
            if month >= startmonth and month <= endmonth:
                count = count + 1
        return count

n= int(input())
leaveList =[]
while n :
    leaveId = int(input())
    leaveType = input()
    noOfDays = int(input())
    dateOfApplication = input()
    leaveList.append(Leave(leaveId,leaveType,noOfDays,dateOfApplication))
    n-=1
    
EL = int(input())
CL = int(input())
SL = int(input())
leaveBalance = {"EL":EL,"CL":CL,"SL":SL}

employee = Employee(leaveList,leaveBalance)
employee.getUpdatedLeaveBalance()

startMonth = int(input())
endMonth = int(input())
count = employee.getLeaveCount(startMonth,endMonth)

if count:
    print(count)
else :
    print("No leave applied between given months")
    
'''
5
1011
CL
1
12-02-21
1012
CL
2
13-04-21
1013
EL
3
13-08-21
1014
EL
2
23-11-21
1015
SL
1
24-12-21
20
4
31
4
8

5
1011
CL
1
13-01-21
1012
CL
4
23-03-21
1013
EL
5
25-05-21
1014
SL
2
27-08-21
1015
CL
1
04-09-21
20
5
30
10
12
'''
