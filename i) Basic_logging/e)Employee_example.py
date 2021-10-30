import logging
logging.basicConfig(level=logging.INFO,filename="Employee.log",format="%(levelname)s:%(message)s")
class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        logging.info(f"Employee created {self.fullname()}, with salary {self.pay} and email {self.email()}")
    def email(self):
        return (f"{self.first}{self.last}@email.com")
    def fullname(self):
        return (self.first+" "+self.last)

emp_1=Employee("John","smith",10000)
emp_1=Employee("Ram","sham",14939291)
emp_1=Employee("John","dinesh",10000)





