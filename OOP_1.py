class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        list_well = ''
        list_well_end = ''
        sum_rating = 0
        num_rating = 0

        for key, item in self.grades.items():
            sum_rating = sum_rating + sum(item)
            num_rating = num_rating + len(item)
        average_rating = sum_rating / num_rating

        i = 0
        while i < len(self.courses_in_progress):
            if i == 0:
                list_well = self.courses_in_progress[i]
            else:
                list_well = list_well + ', ' + self.courses_in_progress[i]
            i += 1
        i = 0
        while i < len(self.finished_courses):
            if i == 0:
                list_well_end = self.finished_courses[i]
            else:
                list_well_end = list_well_end + ', ' + self.finished_courses[i]
            i += 1

        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_rating}\nКурсы в процессе изучения: {list_well}\nЗавершенные курсы: {list_well_end}"

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.lectures_attached:
            if course in lecturer.lecture_grades:
                lecturer.lecture_grades[course] += [grade]
            else:
                lecturer.lecture_grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.lectures_attached = []
        self.lecture_grades = {}

    def __str__(self):
        sum_rating = 0
        num_rating = 0

        for key, item in self.lecture_grades.items():
            sum_rating = sum_rating + sum(item)
            num_rating = num_rating + len(item)
        average_rating = sum_rating / num_rating

        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_rating}"


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Ruby']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Anatoli', 'Vaserman')
cool_lecturer.lectures_attached += ['Ruby']
cool_lecturer.lectures_attached += ['Git']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Ruby', 10)

best_student.rate_hw(cool_lecturer, 'Ruby', 9)
best_student.rate_hw(cool_lecturer, 'Ruby', 8)
best_student.rate_hw(cool_lecturer, 'Git', 8)

# print(best_student.grades)
# print(cool_lecturer.lecture_grades)
print(cool_reviewer.__str__())
