class Employee:

    def __init__(self, name='', date_of_birth='', starting_date='', ssn=0, phone_number=0):
        self.name = name
        self.date_of_birth = date_of_birth
        self.starting_date = starting_date
        self.ssn =  ssn
        self.phone_number = phone_number

    def setName(self, name):
        self.name = name

    def setDate_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth

    def setStarting_date(self, starting_date):
        self.starting_date = starting_date

    def setSsn(self, ssn):
        self.ssn =  ssn

    def setPhone_number(self, phone_number):
        self.phone_number = phone_number

    def getName(self):
        return self.name

    def getDate_of_birth(self):
        return self.date_of_birth

    def getStarting_date(self): 
        return self.starting_date

    def getSsn(self):
        return self.ssn

    def getPhone_number(self):
        return self.ssn

    def print(self):
        print('\n\nEmployee name:', self.name, '\nBorn on:', self.date_of_birth, '\nStarted on:', self.starting_date, '\nSsn:', self.ssn, '\nPhone:', self.phone_number)


class Hourly_Based_Employee(Employee):

    def __init__(self, name='', date_of_birth='', starting_date='', ssn=0, phone_number=0, per_hour=0, hours=0):
        Employee.__init__(self, name, date_of_birth, starting_date, ssn, phone_number)
        self.per_hour = per_hour
        self.hours = hours

    def setPer_hour(self, per_hour):
        self.per_hour = per_hour

    def setHours(self, hours):
        self.hours = hours

    def getPer_hours(self):
        return self.per_hour

    def getHours(self):
        return self.hours

    def compute_salary(self):
        return (self.per_hour * self.hours)

    def print(self): 
        print('\n\nEmployee name:', self.name, '\nBorn on:', self.date_of_birth, '\nStarted on:', self.starting_date, '\nSsn:', self.ssn, '\nPhone:', self.phone_number, '\nRate:', self.per_hour, '\nScheduled hours:', self.hours)


class Salary_Based_Employee(Employee):

    def __init__(self, name='', date_of_birth='', starting_date='', ssn=0, phone_number=0, salary=0):
        Employee.__init__(self, name, date_of_birth, starting_date, ssn, phone_number)
        self.salary = salary

    def setSalary(self, salary): self.salary = salary

    def getSalary(self):
        return self.salary

    def compute_salary(self):
        return self.salary  # ??? what is this

    def print(self):
        print('\n\nEmployee name:', self.name, '\nBorn on:', self.date_of_birth, '\nStarted on:', self.starting_date, '\nSsn:', self.ssn, '\nPhone:', self.phone_number, '\nSalary', self.salary)


class Manager_Employee(Salary_Based_Employee):

    def __init__(self, name='', date_of_birth='', starting_date='', ssn=0, phone_number=0, salary=0, bonus=0):
        Salary_Based_Employee.__init__(self, name, date_of_birth, starting_date, ssn, phone_number, salary)
        self.bonus = bonus

    def setBonus(self, bonus):
        self.bonus = bonus

    def getBonus(self):
        return self.bonus

    def compute_salary(self):
        return self.salary + self.bonus

    def print(self):
        print('\n\nEmployee name:', self.name, '\nBorn on:', self.date_of_birth, '\nStarted on:', self.starting_date, '\nSsn:', self.ssn, '\nPhone:', self.phone_number, '\nSalary', self.salary, '\nBonus:', self.bonus)
