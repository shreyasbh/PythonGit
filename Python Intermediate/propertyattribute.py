class Employee(object):
    def __init__(self,first,last):
        self.first = first
        self.last = last
        
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
     
    @property 
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
        
    @fullname.setter
    def fullname(self,name):
        first, last = name.split(" ")
        self.first = first
        self.last = last
        
    @fullname.deleter
    def fullname(self,name):
        print("deleteing name")
        self.first = None
        self.last = None
        
    
emp1 = Employee("Shreyas", "B")
emp1.last = "D"
emp1.fullname("Shreyas Bhagavath")
del emp1.fullname
print(emp1.first)
print(emp1.last)
print(emp1.email)
