from payroll_system import Employee, Department

# Example usage:
if __name__ == "__main__":
    employee1 = Employee(1, "John", "Doe", "Manager", 50000)
    employee2 = Employee(2, "Jane", "Smith", "Developer", 40000)

    it_department = Department(101, "IT", "New York")
    it_department.add_employee(employee1)
    it_department.add_employee(employee2)

    it_department.display_employees()
