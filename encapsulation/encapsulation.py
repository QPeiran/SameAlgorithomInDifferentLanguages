########## overview play ground ################

'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.


class Person:
  def __init__(self, fname = "DefaultF", lname = "DefaultL"):
    self.firstname = fname
    self.lastname = lname

  def printname(this):
    print(this.firstname, this.lastname)

class Student(Person):
  def __init__(self, fname = "DefaultF2", lname = "DefaultL2", age = "DefaultA"):
    Person.__init__(self, fname , lname )   
    self.age = age

  def printage(self, texts):
    print(self.age, texts)
    

x = Student("Mike", "Olsen", 19)
x.printname()
x.printage("yrs old")

# Python program to  
# demonstrate private members 
  
# Creating a Base class 
class Base: 
    def __init__(self): 
        self.a = "init public in Base"
        self.__c = "init private in Base"
  
# Creating a derived class 
class Derived(Base): 
    def __init__(self): 
          
        # Calling constructor of 
        # Base class 
        Base.__init__(self)  
        print("Calling private member of base class: ") 
        #print(self.__a) 
# Driver code 
obj1 = Base() 
print(obj1.a) 

obj2 = Derived()
# Uncommenting print(obj1.c) will 
# raise an AttributeError 
  
# Uncommenting obj2 = Derived() will 
# also raise an AtrributeError as 
# private member of base class  
# is called inside derived class 
'''
class Hello:
    def __init__(self, name):
        self.a = 10
        self._b = 20
        self.__c = 30
    def set_value(self, value):
        #self.a = value
        #self._b = value
        self.__c = value
    def get_value(self):
        #return self.a
        #return self._b
        return self.__c
        
    def fun(self):
        print("Public method")
    def __fun(self):
        print("Private method")
        
hello = Hello("World")
hello.a = 25
print(hello.a) # 25
hello._b = 50
print(hello._b) # 50

#print(hello.__c) #broken

print(hello.get_value()) # 30

hello.set_value(100)
print(hello.get_value()) # 100

hello.fun()
#hello.__fun() # broken
      
########## protected ###############



class Base: 
    def __init__(self): 
          
        # Protected member 
        self._a = 2
    def _hello(self):
        print("hello")
  
# Creating a derived class     
class Derived(Base): 
    def __init__(self): 
          
        # Calling constructor of 
        # Base class 
        Base.__init__(self)  
        print("Calling protected member of base class: ") 
        print(self._a) 
          
obj1 = Base() 
obj1._hello()
# Calling protected member 
# Outside class will  result in  
# AttributeError 
#print(obj1.a) 
  
obj2 = Derived() 


############ private ##########
