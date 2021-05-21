# преподаватели бывают разные, поэтому теперь класс Mentor должен стать родительским классом,
# а от него нужно реализовать наследование классов Lecturer (лекторы) и
# Reviewer (эксперты, проверяющие домашние задания).
# Очевидно, имя, фамилия и список закрепленных курсов логично реализовать на уровне родительского класса.

# В квизе к предыдущей лекции мы реализовали возможность выставлять студентам оценки за домашние задания.
# Теперь это могут делать только Reviewers (реализуйте такой метод)!
# А что могут делать лекторы? Получать оценки за лекции от студентов :)
# Реализуйте метод выставления оценок лекторам у класса Student
# (оценки по 10-балльной шкале, хранятся в атрибуте-списке).
# Лектор при этом должен быть закреплен за тем курсом, на который записан студент.
#
# Перегрузите магический метод __str__ у всех классов.
# Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов
# по средней оценке за лекции и студентов по средней оценке за домашние задания.

# !!!!!!!!!!!!!!!!!!!!доделать
#  !!!!!посмотри магический метод compare!!!!!!!!

# Создайте по 2 экземпляра каждого класса, вызовите все созданные методы, а также реализуйте две функции:
#
# для подсчета средней оценки за домашние задания по всем студентам в рамках
# конкретного курса (в качестве аргументов принимаем список студентов и название курса);
# для подсчета средней оценки за лекции всех лекторов в рамках конкретного курса
# (в качестве аргументов принимаем список лекторов и название курса).

from statistics import mean

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade_from_students):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade_from_students]
            else:
                lecturer.grades[course] = [grade_from_students]
        else:
            return 'Ошибка'

    # def average_rate_student(self, grades):
    #     grades_list = []
    #     for key, value in grades.items():
    #         for v in value:
    #             grades_list.append(v)
    #     average_rate_student = mean(grades_list)
    #
    #     return average_rate_student

    def __str__(self):
        correct_output = f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {average_rate(self.grades)}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}"
        return correct_output

    def __lt__(self, other_student):
        return compare_in_class(self, other_student, Student)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    # def average_rate_1(self, grades_from_students):
    #     average_rate = mean(grades_from_students)
    #     return average_rate

    def __str__(self):
        correct_output = f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {average_rate(self.grades)}"
        return correct_output

    def __lt__(self, other_lecturer):
        return compare_in_class(self, other_lecturer, Lecturer)

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        correct_output = f"Имя: {self.name} \nФамилия: {self.surname}"
        return correct_output


def average_rate(grades):
    grades_list = []
    for key, value in grades.items():
        for v in value:
            grades_list.append(v)
    average_rate_ = mean(grades_list)

    return average_rate_


def compare_in_class(class1, class2, estimated_class):
    if isinstance(class2, estimated_class):
        person_compared1 = f'{class1.name} {class1.surname}'
        person_compared2 = f'{class2.name} {class2.surname}'
        if average_rate(class1.grades) > average_rate(class2.grades):
            answer = f'{person_compared1} имеет лучший средний балл, чем {person_compared2}'
        elif average_rate(class1.grades) == average_rate(class2.grades):
            answer = f'{person_compared1} и {person_compared2} равны по среднему баллу'
        else:
            answer = f'{person_compared2} имеет лучший средний балл, чем {person_compared1}'
        return answer
    else:
        return "Ошибка"

# def compare_lecturer(class1, class2, Lecturer):
#     if isinstance(class2, Lecturer):
#         person_compared1 = f'{class1.name} {class1.surname}'
#         person_compared2 = f'{class2.name} {class2.surname}'
#         if class1.average_rate_student(class1.grades) > class2.average_rate_student(class2.grades):
#             answer = f'{person_compared1} имеет лучший средний балл, чем {person_compared2}'
#         elif class1.average_rate_student(class1.grades) == class2.average_rate_student(class2.grades):
#             answer = f'{person_compared1} и {person_compared2} равны по среднему баллу'
#         else:
#             answer = f'{person_compared2} имеет лучший средний балл, чем {person_compared1}'
#         return answer
#     else:
#         return "Ошибка"

def average_rate_for_course(person_list, course_name, estimated_class):
    grades = []
    for i in range(len(person_list)):
        if not isinstance(person_list[i], estimated_class):
            return 'Некорректный ввод'
        if course_name in person_list[i].grades.keys():
            grades += person_list[i].grades[course_name]
    result = f'средний балл за курс {course_name} среди {estimated_class.__name__} составляет: {average_rate({course_name: grades})}'
    return result


best_student = Student('Jane', 'Austen', 'female')
best_student.courses_in_progress += ['Python']

ordinary_student = Student('Oksana', 'Denisova', 'female')
ordinary_student.courses_in_progress += ['Python']
ordinary_student.courses_in_progress += ['Git']
ordinary_student.courses_in_progress += ['Java Script']

cool_lecturer = Lecturer('James', 'Benwick')
cool_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('Anne', 'Elliot')
cool_reviewer.courses_attached += ['Python']

one_more_lecturer = Lecturer('Frederic', 'Wentworth')
one_more_lecturer.courses_attached += ['Java Script']

one_more_reviewer = Reviewer('Charles', 'Musgrove')
one_more_reviewer.courses_attached += ['Java Script']

one_more_more_reviewer = Reviewer('Mary', 'Musgrove')
one_more_more_reviewer.courses_attached += ['Git']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
one_more_reviewer.rate_hw(best_student, 'Java Script', 10)
one_more_more_reviewer.rate_hw(best_student, 'Git', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer.rate_hw(ordinary_student, 'Python', 6)
cool_reviewer.rate_hw(ordinary_student, 'Python', 10)
cool_reviewer.rate_hw(ordinary_student, 'Python', 8)
one_more_reviewer.rate_hw(ordinary_student, 'Java Script', 7)
one_more_more_reviewer.rate_hw(ordinary_student, 'Git', 8)

print(average_rate(best_student.grades))
print(average_rate(ordinary_student.grades))


best_student.rate_lecturer(cool_lecturer, 'Python', 10)
ordinary_student.rate_lecturer(cool_lecturer, 'Python', 10)

best_student.rate_lecturer(one_more_lecturer, 'Java Script', 10)
ordinary_student.rate_lecturer(one_more_lecturer, 'Java Script', 10)

print(average_rate(cool_lecturer.grades))
print(average_rate(one_more_lecturer.grades))

print(best_student.grades)
print(ordinary_student.grades)

print(f'Студенты оценили работу {cool_lecturer.name} {cool_lecturer.surname} на {average_rate(cool_lecturer.grades)} баллов')
print(f'Студенты оценили работу {one_more_lecturer.name} {one_more_lecturer.surname} на {average_rate(one_more_lecturer.grades)} баллов')

print('')
print(best_student)
print('')
print(ordinary_student)
print('')
print(cool_lecturer)
print('')
print(cool_reviewer)

course1 = 'Python'
print(average_rate_for_course([best_student, ordinary_student], course1, Student))
course2 = 'Java Script'
print(average_rate_for_course([best_student, ordinary_student], course2, Student))
print('')
print(average_rate_for_course([cool_lecturer, one_more_lecturer], course1, Lecturer))
print(average_rate_for_course([cool_lecturer, one_more_lecturer], course2, Lecturer))
print('')
print(cool_lecturer < one_more_lecturer)
print(one_more_lecturer < cool_lecturer)
print('')
print(best_student < ordinary_student)
