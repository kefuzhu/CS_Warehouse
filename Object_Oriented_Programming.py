class Employee:

    # Initialize the object
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        # self.email = first + " " + last + "@email.com" ## This line is improved by setting it with property decorator
        self.pay = pay

    # Implicit representation of the object
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    # Explicit representation of the object
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    # Define Employee() + Employee()
    def __add__(self, other):
        return self.pay + other.pay

    # Define len(Employee())
    def __len__(self):
        return len(self.fullname())

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # When setting the fullname property, it will be called automatically to update the first and last name
    @fullname.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # Define del(Employee().fullname), automatically delete the fullname property as well as setting first and last name to None
    @full_name.deleter
    def fullname(self):
        print('Delete Name: {}!'.format(self.fullname))
        self.first = None
        self.last = None

    def apply_bonus(self):
        self.pay = self.pay + self.raise_amount

    @classmethod  # Class method
    def set_raise_amount(cls, amount):
        cls.set_raise_amount = amount

    @staticmethod  # Static method works just like normal functions and is not necessarilly related to this class
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Kefu', 'Zhu', 60000)
emp_1.full_name = 'Kefu Zhu'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
print(emp_1.fullname)
