class Teacher:
    def __init__(self, name: str, students, salary):
        self.name = name
        self.students = students
        self.salary = salary

    def teach(self):
        self.salary = f"{3 * self.students / 1.5} dollars"
        print(self.salary)


    def accept_exam(self):
        pass
    def __str__(self):
        return f"Профессор {self.name}, кількість студентів: {self.students}, зарплата: {self.salary} dollars"



class Professor:
    def write_science_work(self):
        pass

class Dean:
    def organize_faculty(self):
        pass



class Rector(Teacher, Professor, Dean):
    def __init__(self, name: str, students, salary):
        super().__init__(name, students, salary)


    def accept_exam(self):
        # implementation
        pass

    def write_science_work(self):
        # implementation
        pass

    def organize_faculty(self):
        # implementation
        pass

if __name__ == "__main__":
    boris = Rector(name="Борис", students=2000, salary=3000)
    boris.teach()