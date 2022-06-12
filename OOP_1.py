list_students = [
    {
        'name': 'Yuriy',
        'surname': 'Bonderenko',
        'gender': 'your_gender',
        'finished_courses': ['Введение в программирование'],
        'courses_in_progress': ['PHP', 'Python', 'JavaScript'],
        'grades': {'PHP': [8, 9, 7, 10, 8],  'Python': [10, 5, 7, 10, 10], 'JavaScript': [8, 7, 10, 10, 6]}
    },
    {
        'name': 'Vasilii',
        'surname': 'Kononenko',
        'gender': 'your_gender',
        'finished_courses': ['Введение в программирование'],
        'courses_in_progress': ['PHP', 'Python', 'JavaScript'],
        'grades': {'PHP': [6, 9, 8, 9, 8],  'Python': [8, 7, 10, 10, 5], 'JavaScript': [7, 8, 10, 10, 8]}
    },
    {
        'name': 'Artem',
        'surname': 'Poloniankin',
        'gender': 'your_gender',
        'finished_courses': ['Введение в программирование'],
        'courses_in_progress': ['PHP', 'Python', 'JavaScript'],
        'grades': {'PHP': [6, 9, 10, 7, 9],  'Python': [7, 9, 9, 10, 7], 'JavaScript': [9, 8, 7, 10, 10]}
    },
]

list_lecturer = [
    {
        'name': 'Oleg',
        'surname': 'Buligin',
        'gender': 'your_gender',
        'courses_attached': ['PHP', 'Python', 'JavaScript'],
        'lecture_grades': {'PHP': [6, 9, 10, 7, 9],  'Python': [7, 9, 9, 10, 7], 'JavaScript': [9, 8, 7, 10, 10]}
    },
    {
        'name': 'Anatolii',
        'surname': 'Vaserman',
        'gender': 'your_gender',
        'courses_attached': ['PHP', 'Python', 'JavaScript'],
        'lecture_grades': {'PHP': [8, 9, 7, 10, 8],  'Python': [10, 5, 7, 10, 10], 'JavaScript': [8, 7, 10, 10, 6]}
    },
    {
        'name': 'Vadim',
        'surname': 'Degtiarev',
        'gender': 'your_gender',
        'courses_attached': ['PHP', 'Python', 'JavaScript'],
        'lecture_grades': {'PHP': [6, 9, 8, 9, 8],  'Python': [8, 7, 10, 10, 5], 'JavaScript': [7, 8, 10, 10, 8]}
    },
]


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
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
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
        super().__init__(name, surname)
        self.lecture_grades = {}

    def __str__(self):
        sum_rating = 0
        num_rating = 0

        for key, item in self.lecture_grades.items():
            sum_rating = sum_rating + sum(item)
            num_rating = num_rating + len(item)
        self.average_rating = sum_rating / num_rating

        return f"Имя: {self.name}\nФамилия: {self.surname}\Курсы: {self.courses_attached}\nСредняя оценка за лекции: {self.average_rating}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Not a lecture")
            return
        return print(self.average_rating < other.average_rating)


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


def student_comparison(list_stud, course):
    total_score = []
    sum_len_dic = 0
    index = 0
    for student in list_stud:
        if course in student['grades']:
            for key, item in student['grades'].items():
                if key == course:
                    total_score = total_score + item
                    index += 1
    sum_len_dic = sum(total_score) / len(total_score)
    print(
        f'Средней оценки за домашние задания по всем студентам в рамках курса "{course}" равна {sum_len_dic}.')


def lecturer_comparison(list_lect, course):
    total_score = []
    sum_len_dic = 0
    index = 0
    for lectur in list_lect:
        if course in lectur['lecture_grades']:
            for key, item in lectur['lecture_grades'].items():
                if key == course:
                    total_score = total_score + item
                    index += 1
    sum_len_dic = sum(total_score) / len(total_score)
    print(
        f'Средней оценки за лекции всех лекторов в рамках курса "{course}" равна {sum_len_dic}.')


student_comparison(list_students, "PHP")
lecturer_comparison(list_lecturer, "Python")

best_student = Student('Yuriy', 'Bonderenko', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Ruby']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

best_2_student = Student('Ruoy', 'Eman', 'your_gender')
best_2_student.courses_in_progress += ['Python']
best_2_student.courses_in_progress += ['JavaScript']
best_2_student.courses_in_progress += ['Git']
best_2_student.courses_in_progress += ['PHP']
best_2_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']
cool_reviewer.courses_attached += ['JavaScript']

cool_lecturer = Lecturer('Anatoli', 'Vaserman')
cool_lecturer.courses_attached += ['Ruby']
cool_lecturer.courses_attached += ['Git']

cool_2_lecturer = Lecturer('Oleg', 'Buligin')
cool_2_lecturer.courses_attached += ['JavaScript']
cool_2_lecturer.courses_attached += ['PHP']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Git', 9)
cool_reviewer.rate_hw(best_student, 'Ruby', 7)

cool_reviewer.rate_hw(best_2_student, 'Python', 8)
cool_reviewer.rate_hw(best_2_student, 'JavaScript', 9)
cool_reviewer.rate_hw(best_2_student, 'PHP', 7)

best_student.rate_hw(cool_lecturer, 'Ruby', 9)
best_student.rate_hw(cool_lecturer, 'Ruby', 10)
best_student.rate_hw(cool_lecturer, 'Git', 8)

best_2_student.rate_hw(cool_2_lecturer, 'JavaScript', 10)
best_2_student.rate_hw(cool_2_lecturer, 'JavaScript', 10)
best_2_student.rate_hw(cool_2_lecturer, 'PHP', 9)

# print(best_student)
# print(cool_lecturer)
# print(cool_2_lecturer)

# print(list_students)

# print(best_2_student.grades)
# print(cool_2_lecturer.lecture_grades)
# print(cool_lecturer.__str__())
# print(cool_2_lecturer.__str__())
# print(best_student.grades > best_2_student.grades)
# cool_lecturer.__lt__(cool_2_lecturer)
