class Student:

    def __init__(self, name: str, laziness, skill=0):
        self.name = name
        self.laziness = laziness
        self.skill = skill


    def go_to_lectures(self):
        while self.laziness <= 100:
            self.skill += 1
            self.laziness += 10
            print(f"Я студент {self.name}, мій скілл: {self.skill}, мій рівень ліні: {self.laziness}")
        if self.laziness >= 100:
            return self.party()




    def party(self):
        while self.laziness > 20:
            print("Настав час напитися")
            self.laziness -= 5.5
            print(f"laziness = {self.laziness}")
        if self.laziness <= 19:
            print(f"Я студент {self.name}, мій скілл: {self.skill}, мій рівень ліні: {self.laziness}")

    def __str__(self):
        return f"Студент:{self.name}, середній бал: {self.skill}"







class Teacher:
    def __init__(self, name: str, students, salary):
        self.name = name
        self.students = students
        self.salary = salary

    def teach(self):
        self.salary = f"{3 * self.students / 1.5} dollars"
        return self.salary


    def accept_exam(self):
        pass
    def __str__(self):
        return f"Профессор {self.name}, кількість студентів: {self.students}, зарплата: {self.salary} dollars"



class DataBaseSaver:

    @staticmethod
    def save(obj, filename):
        file = open(filename, "w")
        file.write(str(obj))
        file.close()




petro = Student(name="Петро", laziness=45, skill=15)
petro.go_to_lectures()

vladimir = Teacher(name="Володимир", students=25, salary=4)


data_service = DataBaseSaver()
data_service.save(petro, "students.txt")
data_service.save(vladimir, "teachers.txt")


