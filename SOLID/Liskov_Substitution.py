class Student:

    def __init__(self, name: str, laziness, skill=0):
        self.name = name
        self.laziness = laziness
        self.skill = skill
        self.personal_data = {}

    def set_personal_data(self, eyecolor, bloodtype, city):
        self.personal_data = {"Колір очей": eyecolor, "Група крові": bloodtype, "Місто": city}

    def get_personal_data(self):
        return self.personal_data

    def go_to_lectures(self):
        while self.laziness <= 100:
            self.skill += 1
            self.laziness += 10
            print(f"Я студент {self.name}, мій скілл: {self.skill}, мій рівень ліні: {self.laziness}")
        if self.laziness >= 100:
            return self.party()

    def pass_exam(self):
        print(f"Я студент {self.name}. Здаю екзамен на вибір факультета")

    def party(self):
        while self.laziness > 20:
            print("Настав час напитися")
            self.laziness -= 5.5
            print(f"laziness = {self.laziness}")
        if self.laziness <= 19:
            print(f"Я студент {self.name}, мій скілл: {self.skill}, мій рівень ліні: {self.laziness}")

    def __str__(self):
        return f"Студент:{self.name}, середній бал: {self.skill}"


class BioStudent(Student):
    def __init__(self, name, laziness, bio_skill: int):
        super().__init__(name, laziness)
        self.skill = bio_skill

    def go_to_lectures(self):
        while self.laziness <= 100:
            self.skill += 1
            self.laziness += 10
            print(f"Я студент {self.name}, мій біоскілл: {self.skill}, мій рівень ліні: {self.laziness}")
        if self.laziness >= 100:
            return self.party()

    def party(self):
        while self.laziness > 20:
            print("Настав час напитися")
            self.laziness -= 5
            print(f"laziness = {self.laziness}")
        if self.laziness <= 19:
            print(f"Я студент {self.name}, мій біоскілл: {self.skill}, мій рівень ліні: {self.laziness}")

    def pass_exam(self):
        print(f"Passing biology exams, bioskill = {self.skill * 2}")


class MathStudent(Student):
    def __init__(self, name, laziness, math_skill: float):
        super().__init__(name, laziness)
        self.skill = math_skill

    def go_to_lectures(self):
        while self.laziness <= 100:
            self.skill += 1
            self.laziness += 10
            print(f"Я студент {self.name}, мій математичний скілл: {self.skill}, мій рівень ліні: {self.laziness}")
        if self.laziness >= 100:
            return self.party()

    def party(self):
        while self.laziness > 20:
            print("Настав час напитися")
            self.laziness -= 5.5
            print(f"laziness = {self.laziness}")
        if self.laziness <= 19:
            print(f"Я студент {self.name}, мій математичний скілл: {self.skill}, мій рівень ліні: {self.laziness}")

    def pass_exam(self):
        print(f"Passing math exams, mathskill = {self.skill * 2}")


class Teacher:
    def __init__(self, name: str, students, salary):
        self.name = name
        self.students = students
        self.salary = salary

    def set_personal_data(self, eyecolor, bloodtype, city):
        self.personal_data = {"Колір очей": eyecolor, "Група крові": bloodtype, "Місто": city}

    def get_personal_data(self):
        return self.personal_data

    def teach(self):
        self.salary = f"{3 * self.students / 1.5} dollars"

    def accept_exam(self):
        pass

    def __str__(self):
        return f"Профессор {self.name}, кількість студентів: {self.students}, зарплата: {self.salary} dollars"


marina = BioStudent(name="Марина", laziness=5, bio_skill=17)



marko = MathStudent(name="Марко", laziness=50, math_skill=14.4)


vladimir = Teacher(name="Володимир", students=25, salary=4)

petro = Student(name="Петро", laziness=45, skill=15)

auditorium_3 = [marina, marko, vladimir, petro]


def find_from_Odesa(auditorium):
    from_odessa = 0
    for o in auditorium:
        if o.get_personal_data()["Місто"] == "Одеса":
            from_odessa += 1
    print(f"From Odesa = {from_odessa}")


def find_from_Jitomir(auditorium):
    from_odessa = 0
    for o in auditorium:
        if o.get_personal_data()["Місто"] == "Житомир":
            from_odessa += 1
    print(f"From Jitomir = {from_odessa}")





if __name__ == "__main__":
    marina.set_personal_data("blue", "4-", "Житомир")
    marko.set_personal_data("green", "4-", "Житомир")
    vladimir.set_personal_data("green", "3-", "Одеса")
    petro.set_personal_data("brown", "2+", "Київ")
    find_from_Odesa(auditorium_3)
    find_from_Jitomir(auditorium_3)
    for i in auditorium_3:
        print(f"Персональні дані {i.name}: {i.get_personal_data()}")


