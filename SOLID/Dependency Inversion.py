class Student:
    def __init__(self, name):
        self.name = name
    def check_in(self):
        print(f"Student {self.name} checked in")

class Teacher:
    def __init__(self, name):
        self.name = name

    def check_in(self):
        print(f"Teacher {self.name} checked in")

class Group:
    def __init__(self, auditorium_no, group_no):
        self.auditorium_no = auditorium_no
        self.group_no = group_no
    def lecture_check_in(self, list_to_check_in: list):
        print(f"Group {self.group_no}; Auditorium: {self.auditorium_no}; Checked in:")
        for person in list_to_check_in:
            person.check_in()
        print(f"Check in for group {self.group_no}, auditorium {self.auditorium_no} is over; Total checked in: {len(list_to_check_in)}")

petro = Student("Петро")
wolodymyr = Teacher("Володимир")
marina = Student("Марина")
evhen = Student("Євген")
alya = Student("Аля")

list_of_people = [petro, wolodymyr, marina, evhen, alya]

group4 = Group(4, 5)


if __name__ == "__main__":
    group4.lecture_check_in(list_of_people)