# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 19:05:48 2018

@author: disiz
"""
"""class BaseClass:
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class"""
##assignmnet 4 question 1.1 
class Polygon: #Parent class
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def enterSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def showSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
            
class Triangle(Polygon): #Subclass(Parentclass)
    def __init__(self):
        Polygon.__init__(self,3)

    def calArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)
t = Triangle()
t.enterSides()
t.showSides()
t.calArea()
print("-"*100)
print('\n')
"""
-Session 4
-Assignment four
"""
##assignmnet 4 question 1.2
def filter_long_words(collection,n):
    long_words=[]
    print("list of words with length greater than %d:"%n)
    for c in collection:
        if len(c)>n:
            long_words.append(c)
    return long_words
lst=['abc','abcde','ab','abcdef','awsedfgt','a','awsde','asedfgthik','asd','wdfgthyju']
input_n=int(input("enter an integer:"))
print(filter_long_words(lst,input_n))
print("-"*100)
print('\n')
"""
-Session 4
-Assignment four
"""
##assignmnet 4 question 2.1
def col_words(collection):
    len_words=[]
    for c in collection:
            len_words.append(len(c))
    return len_words
lst=['abc','abcde','ab','abcdef','awsedfgt','a']
print(lst)
print("length of words in given list:",col_words(lst)) 
print("-"*100)
print('\n')
"""
-Session 4
-Assignment four
"""           
# defining a function to find whether character is vowel or not
##assignmnet 4 question 2.2
def isvowel(alphabet):
    vowels=['a','e','i','o','u']
    if alphabet.lower() in vowels:
        return True
    else:
        return False
x=str(input("enter an character:"))
print(isvowel(x))
print("-"*100)
y=str(input("enter one more character:"))
print(isvowel(y))
print("-"*100)
print('\n')
print("End of assignment")

