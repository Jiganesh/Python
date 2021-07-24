class College:
    def __init__(self, collegeId, Name, City, Rating):
        self.collegeId = collegeId
        self.Name = Name
        self.City = City
        self.Rating = Rating

class University:
    def __init__(self , universityName , collegeCollection):
        self.universityName = universityName
        self.collegeCollection = collegeCollection

    def findCollegeByCity(self, city):
        for i in self.collegeCollection:
            if i.City == city:
                return i
        return None     

    def sortCollegeByRating(self):

        if self.collegeCollection:
            lista = sorted(self.collegeCollection,key = lambda x: x.Rating, reverse = False)
            return lista
        else:
            return None

n = int(input())
clist =[]
while n:
    cid =int(input())
    cname = input()
    ccity = input()
    crating = float(input())
    clist.append(College(cid,cname,ccity,crating))
    n -= 1
city = input()
university = University("university", clist)
college = university.findCollegeByCity(city)
if college:
    print(college.collegeId, college.Name, college.City, college.Rating, sep="\n")

listsorted = university.sortCollegeByRating()
for i in listsorted:
    print(i.collegeId)


'''
4
101
col1
AHD
3.5
102
col2
BLR
4.4
103
col3
KOL
5.0
104
col4
TVM
3.7
BLR
'''
    
