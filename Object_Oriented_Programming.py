class Employee:

    # Initialize the object
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        # self.email = first + " " + last + "@email.com" ## This line is improved by setting it with property decorator
        # self.fullname = first + " " + last ## This line is improved by setting it with property decorator
        self.pay = pay

    # Implicit representation of the object, can be accessed by repr()
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    # Explicit representation of the object, can be accessed by str()
    def __str__(self):
        return '{} - {}'.format(self.fullname, self.email)

    # Define Employee() + Employee()
    def __add__(self, other):
        return self.pay + other.pay

    # Define len(Employee())
    def __len__(self):
        return len(self.fullname())

    @property  # This will define additional attributes for the class
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property  # This will define additional attributes for the class
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # Setter functions need to be implemented in order to change the attribute defined with @property
    # When setting the fullname property, the setter function will be called automatically to update the first and last name
    @fullname.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # Define del(Employee().fullname), automatically delete the fullname property as well as setting first and last name to None, pay to 0
    @full_name.deleter
    def fullname(self):
        print('Delete Name: {}!'.format(self.fullname))
        self.first = None
        self.last = None
        self.pay = 0

    def apply_bonus(self):
        self.pay = self.pay + self.raise_amount

    # Class method: Receive the class as the first argument instead of the instance (e.g. Employee.set_raise_amount(1.05))
    @classmethod
    def set_raise_amount(cls, amount):
        cls.set_raise_amount = amount

    @classmethod  # Class method can also be used as constructor, to meet various user cases
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # Static method works just like normal functions and is not necessarilly related to this class. Static method does not access the class/instance anywhere
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# Sub-class of the Employee class (Inheritence)


class Developer(Employee):

    # Initialize the object
    def __init__(self, first, last, pay, prog_lang):
        # Leverage the parent class for initialization, this can also be done with Employee.__init__(self, first, last, pay)
        super().__init__(first, last, pay)

        self.prog_lang = prog_lang


class Manager(Employee):

    # Initialize the object
    def __init__(self, first, last, pay, employees=None):
        # Leverage the parent class for initialization, this can also be done with Employee.__init__(self, first, last, pay)
        super().__init__(first, last, pay)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname)

# # Basic functions for Class
# emp_1 = Employee('Kefu', 'Zhu', 60000)

# print(emp_1)
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname)

# del emp_1.fullname
# print(emp_1.fullname)

# # Class method as constructor, from_string()
# emp_str_2 = 'Xiyang-Xu-60000'
# emp_2 = Employee.from_string(emp_str_2)
# print(type(emp_2))


# # Inheritance - Subclass
# dev_1 = Developer('Kefu', 'Zhu', 60000, 'Python')
# dev_2 = Developer('Kefu', 'Zhu Junior', 30000, 'R')
# mgr_1 = Manager('Xi', 'Yang', 90000, [dev_1])

# print(dev_1)
# print(dev_1.email)
# print(dev_1.prog_lang)

# print(mgr_1.email)

# mgr_1.print_emps()

# print(mgr_1.email)
# mgr_1.add_emp(dev_2)
# mgr_1.print_emps()

# # Setter/Getter methods
# emp_1 = Employee('Kefu', 'Zhu', 60000)
# emp_1.fullname = 'Xiyang Xu'

# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.fullname)

# del (emp_1.fullname)

# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.fullname)
# print(emp_1.pay)
