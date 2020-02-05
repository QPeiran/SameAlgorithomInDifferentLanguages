########## overview ################

class Hello:
    def __init__(self, name):
        self.a = 10
        self._b = 20
        self.__c = 30

hello = Hello("World")
print(hello.a)
print(hello._b)
print(hello.__c)
      
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
