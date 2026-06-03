#abstraction

from abc import ABC,abstractmethod  
class animal(ABC):
  #def abstractmethod()
  @abstractmethod
  def sound(self):
    pass

class dog(animal):

  def sound(self):
    return "woof"

 #define class cat

class cat(animal):
  def sound(self):
    return "meow"

#define object
bruno=dog()
bruno.sound()
tom=cat()
tom.sound()
        
