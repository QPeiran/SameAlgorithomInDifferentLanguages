########## overview play ground ################

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
hello = Hello("World")
hello.a = 25
print(hello.a) # 25
hello._b = 50
print(hello._b) # 50

#print(hello.__c) #broken

print(hello.get_value()) # 30

hello.set_value(100)
print(hello.get_value()) # 100
      
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
