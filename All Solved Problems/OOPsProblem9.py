class MovieCompany:
    def __init__(self, movieCold, movieCompany, awards, noOfMovies, movieCategory):#movieCategory {movieName: Category}
        self.movieCold = movieCold;
        self.movieCompany = movieCompany;
        self.awards = awards;
        self.noofMovies = noOfMovies;
        self.movieCategory = movieCategory;

class MovieSolution:
    def __init__(self,movieList):
        self.movieList = movieList
        #has movieCompany objects

    def getsecondlargestnoofmoviesincategory(self,category):
        array =[]
        for i in self.movieList:
            count =0
            for j in i.movieCategory.values():
                if j == category:
                    count+=1
            if count : array.append([count, i.movieCompany])
        if len(array)<=1:
            return "Not enough companies found in this category"

        array.sort()
        return array[-2][1]
            
    def getmoviesincategory(self,category):
        count =0
        for i in self.movieList:
            for j in i.movieCategory:
                if i.movieCategory[j] == category:
                    count+=1
        if count:
            return count
        else:
            return "No movies found in this category"

array = []

n =int(input())
while n:
    movieCold = int(input())
    company =input()
    awards=input()
    noofmovies = int(input())
    d={}
    while noofmovies:
        genre = input()
        movie = input()
        d[movie]=genre
        noofmovies-=1

    m1 = MovieCompany(movieCold, company, awards, noofmovies, d)
    array.append(m1)
    n-=1
category =input()
h =MovieSolution(array)
print(h.getmoviesincategory(category))
print(h.getsecondlargestnoofmoviesincategory(category))

'''
4
11
Test1
2
5
Thriller
lethalWeapon1
Thriller
lethalWeapon2
Thriller
lethalWeapon3
Thriller
lethalWeapon4
Thriller
lethalWeapon5
12
Test2
2
3
Thriller
BraveHeart1
Crime
BraveHeart2
Thriller
BraveHeart3
13
Test3
2
3
Thriller
RV1
Thriller
RV2
Thriller
RV3
14
Test4
2
6
Thriller
RV1
Thriller
RV2
Thriller
RV3
Thriller
RV4
Thriller
RV5
Thriller
RV6
Thriller
----------------------------------------------
4
11
Test1
1
3
Crime
LW1
Crime
LW2
Crime
LW3
12
Test2
1
3
Pop
BH1
Crime
BH2
Crime
BH3
13
Test3
1
4
Crime
RV1
Crime
RV2
Crime
RV3
Crime
RV4
14
Test4
1
5
Crime
RV1
Crime
RV2
Crime
RV3
Crime
RV4
Crime
RV5
Pop1
'''



        
    