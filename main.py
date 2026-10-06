# Nested class = A class defined within another class
#                class Outer:
#                     class Inner:

# Benefits: Allows you to logically group classes that are closely related
#           Encapsulates private details that aren't relevant outside of the outer class
#           Keeps the namespace clean; reduces the possibility od naming conflicts

class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"Name: {self.name} \tPosition: {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def list_employees(self):
        for employee in self.employees:
            print(employee.get_details())

company = Company("Krusty Krab")
company2 = Company("Chum Bucket")

company.add_employee("Eugene", "Manager")
company.add_employee("Spongebob", "Cook")
company.add_employee("Squidward", "Cashier")

company2.add_employee("Sheldon", "Manager")
company2.add_employee("Karen", "Assistant")

print(company.company_name)
company.list_employees()

print(company2.company_name)
company2.list_employees()