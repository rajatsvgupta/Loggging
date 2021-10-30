import logging
logger=logging.getLogger(__name__)
formatter=logging.Formatter("%(name)s:%(levelname)s:%(message)s")
logger.setLevel(logging.INFO)
file_handler=logging.FileHandler("Employee.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class Employee():
    def __init__(self,first,last):
        self.first=first
        self.last=last
        logger.info(f"employee created with name {self.fullname} and have mail id {self.email}")
    @property
    def fullname(self):
        return(f"{self.first} {self.last}")
    @property
    def email(self):
        return (f"{self.first}.{self.last}@email.com")

emp_1=Employee("Rajat","Gupta")