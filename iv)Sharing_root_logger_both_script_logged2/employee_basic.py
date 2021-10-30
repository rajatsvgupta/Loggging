import logging

logging.basicConfig(filename="Employee.log",level=logging.INFO, format="%(name)s:%(levelname)s:%(message)s")
class Employee():
    def __init__(self,first,last):
        self.first=first
        self.last=last
        logging.info(f"employee created with name {self.fullname} and have mail id {self.email}")
    @property
    def fullname(self):
        return(f"{self.first} {self.last}")
    @property
    def email(self):
        return (f"{self.first}.{self.last}@email.com")

emp_1=Employee("Rajat","Gupta")
