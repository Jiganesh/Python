# Inheritance

class A:

    def feature1(self):
        print("Feature 1 Working")

    def feature2(self):
        print("Feature 2 Working")


class B(A):

    def feature3(self):
        print("Feature 3 Working")

    def feature4(self):
        print("Feature 4 Working")


class C(B):

    def feature5(self):
        print("Feature 5 Working")


splitter = "==================="

a = A()
a.feature1()
a.feature2()

print(splitter)

b = B()
b.feature1()
b.feature2()
b.feature3()
b.feature4()

print(splitter)

c = C()
c.feature1()
c.feature2()
c.feature3()
c.feature4()
c.feature5()


# B(A) : Single Level Inheritance
# C(B) : Multi-Level Inheritance
# C (A,B) : Multiple Inheritance
# B(A), C(A) : Hierarchical Inheritance
# Inheritance Consisting Multiple Types of Inheritance like B(A), C(A), D(B,C)
