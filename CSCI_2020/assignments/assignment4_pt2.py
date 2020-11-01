from assignment4_pt1 import *


emp1 = Hourly_Based_Employee('Jen', '01/11/00', '11/01/14', 444444444, 4444444444, 13, 35)
emp1.print()
print('Salary:', emp1.compute_salary())


emp2 = Salary_Based_Employee('Jack', '11/02/96', '02/11/00', 666666666, 6666666666, 40000)
emp2.print()
print('Salary:', emp2.compute_salary())

emp3 = Manager_Employee('Jess', '02/11/72', '11/02/96', 555555555, 5555555555, 80000, 2000)
emp3.print()
print('Salary:', emp3.compute_salary())