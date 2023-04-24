from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def full_name(self):
        return f'{self.surname.upper()}, {self.name}'
    
    @abstractmethod
    def get_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, name, surname, salary):
        super().__init__(name, surname)
        self.salary = salary

    def get_salary(self):
        return self.salary


class HourlyEmployee(Employee):
    def __init__(self, name, surname, hours_worked, hourly_wage):
        super().__init__(name, surname)
        self.hours_worked = hours_worked
        self.hourly_wage = hourly_wage

    def get_salary(self):
        return self.hours_worked * self.hourly_wage


class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def print(self):
        for e in self.employees:
            print(f'{e.full_name}\t{e.get_salary()}')


def main():
    payroll = Payroll()
    payroll.add_employee(FullTimeEmployee('John', 'Doe', 6000))
    payroll.add_employee(FullTimeEmployee('Jane', 'Doe', 6500))
    payroll.add_employee(HourlyEmployee('Jennifer', 'Smith', 200, 50))
    payroll.add_employee(HourlyEmployee('David', 'Wilson', 150, 100))
    payroll.add_employee(
        HourlyEmployee('John Jacob', 'Jingleheimer-Schmidt', 200, 50))
    payroll.print()
    


if __name__ == '__main__':
    main()
