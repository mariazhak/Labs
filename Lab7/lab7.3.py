class Employee:
    def __init__(self, name, id_number, department):
        self.name = name
        self.id_number = id_number
        self.department = department

    def display(self):
        print('Name: ' + self.name)
        print('ID: ' + self.id_number)
        print('Department: ' + self.department)


emp1 = Employee(input('Enter the name of an employee: '), input('Enter ID of an employee: '),
                input('Enter department of an employee: '))
emp1.display()