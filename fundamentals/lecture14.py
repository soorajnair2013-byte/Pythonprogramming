class parent: #define class
  def __init__(self):   # constructor
  pass

  def details(self):  #method for parent class

  pass


class child1(parent):  #define child class
  def __init__(self):
    pass
    super().__init__(self)
    pass


class child2(child1):  #define child class
  def __init__(self):
    pass
    super().__init__(self)
    pass


#define objectl
obj1.parent()
obj2.child1()
obj3.child2()






class Employee:
    def __init__(self, name, age, position, monthly_salary):
        self.name = name
        self.age = age
        self.__position = position
        self.__monthly_salary = monthly_salary

    def get_position(self):
      return self.__position
    def set_position(self,position):
      self.__position=position

    def get_salary(self):
      return self.__monthly_salary
    def set_salary(self,salary):
      self.__monthly_salary=salary

    def __calculate_annual_salary(self):
      return self.__monthly_salary *12

    def get_annual_salary(self):
      return self.__calculate_annual_salary()

    def display_employee_details(self):
        print(f"""Name: {self.name}, Age: {self.age},
        Position:{self.__position},
            Monthly Salary:{self.__monthly_salary}""")


employee1=Employee("Alice",30,"Developer",5000)
employee2=Employee("Bob",25,"Manager",7500)

print(employee1.age)
print(employee1.get_position())

