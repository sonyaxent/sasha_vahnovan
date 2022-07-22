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





marina = BioStudent(name="Марина", laziness=5, bio_skill=17)
marina.pass_exam()
marina.go_to_lectures()

marko = MathStudent(name="Марко", laziness=50, math_skill=14.4)
marko.pass_exam()
marko.go_to_lectures()



petro = Student(name="Петро", laziness=45, skill=15)

petro.pass_exam()
