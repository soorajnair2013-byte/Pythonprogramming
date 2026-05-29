class bank:
  name_of_bank='TJSB'  #class variable


#define constructor
  def __init__(self,variable1,variable2,variable3):
   self.variable1=variable1   #instance variable
   self.variable2=variable2
   self.variable3=variable3

#method/function
  def method1(self):
   return self.variable1

#method2
#method3

#define obj:class bank
obj1=bank(10,20,30)
print(obj1.variable1)



class paytm:
  
  def __init__(self,balance):
   self.balance=balance
  
  
  def withdraw(self,amount):
    self.amount=amount 

    if self.amount<=self.balance:
      self.balance -=self.amount
      print(f"{self.amount}debited successfully")
    else:
      print("insufficient balance")

  def credit(self,amount):
    self.amount=amount 
    self.balance+=self.amount
    print(f"available balance is {self.balance}")

  def check_balance(self):
    print(f"available balance is: {self.balance}")
   


obj1=paytm(10000)
obj1.withdraw(4000)
obj1.check_balance()
obj1.credit(5000)






#inheritance

class animal:
  def ___init__(self,eyes,legs,ears)
    self.eyes=eyes
    self.legs=legs
    self.ears=ears

class dog(animal):
  def __init__(self,height,size):
    super().__init__(eyes,legs,ears):
    
    self.height=height
    self.size=size

class cat(animal):
  def __init__(self,height,size):
    super().__init__(eyes,legs,ears):
  
    
    self.height=height
    self.size=size

obj.dog(1,2,3,4,5,)   
obj.cat(1,2,3,4,5,)



class bank # parent class
    
    def __init__(self,name,age):  #constructor
     self.name=name
     self.age=age  

class saving (bank)  #child class
      
      

class current(bank)  #child class



class nri (bank)  #child class


class pension(bank)  #child class




