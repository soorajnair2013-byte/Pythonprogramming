#concept  of oops

class employee:
    def __init__(self,name,age,salary,gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender

# def display(self):
#   print(self.name,self.age,self.salary,self.gender)  


emp1=employee('Devesh',25,64646,'male')  
emp2=employee('Ramesh',30,64787,'male')  


print(emp1.name)
print(emp1.age)
print(emp2.salary)
print(emp2.gender)




#constructor

class ITV:
    def __init__(self,
                course,
                 name,
                 age,
                 duration):
        self.course=course
        self.name=name
        self.age=age
        self.duration=duration
   
student1=ITV('JFSD','Namit',22,4)
student2=ITV('DSDA','Sumit',24,6)
student3=ITV('JFSD','Neha',25,8)
student4=ITV('JFSD','Riya',20,2)

print(student1.course)
print(student2.name)
print(student3.age)
print(student4.duration)




class cars:

  engine=1234
  def __init__(self,wheel,model,capacity,colour):
      self.wheel=wheel
      self.model=model
      self.capacity=capacity
      self.colour=colour

  def mileage(self):
    mileage=15
    return mileage


obj1=cars(4,'petrol',4,'red')
print(obj1.wheel)
print(obj1.model)
print(obj1.capacity)
print(obj1.colour)
print(obj1.mileage())
print(cars.engine)


