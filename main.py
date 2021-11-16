class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        """ Add grade from 0 to 10 inside dict grade_lecture class Lecturer """
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress
                and course in lecturer.courses_attached and grade in range(0, 11)):
            if course in lecturer.grade_lecture:
                lecturer.grade_lecture[course] += [grade]
            else:
                lecturer.grade_lecture[course] = [grade]
        else:
            return 'Error'

    def __average_grade(self):
        """ Calculates the average for all grades in all courses"""
        if len(self.grades.values()) != 0:
            grade_list = []
            for v in self.grades.values():
                grade_list.extend(v)
            mean_grade = sum(grade_list) / len(grade_list)
            return mean_grade
        return 'Error'

    def __str__(self):
        res = (f'Имя: {self.name.capitalize()} \n'
               f'Фамилия: {self.surname.capitalize()} \n'
               f'Средняя оценка за домашние задания: {self.__average_grade():.1f} \n'
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'
               f'Завершенные курсы: {", ".join(self.finished_courses)}')
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.__average_grade() < other.__average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        """ Inherit init from parent and add an attribute dict grade_lecture """
        super().__init__(name, surname)
        self.grade_lecture = {}

    def __average_grade(self):
        """ Calculates the average for all grades in all courses"""
        if len(self.grade_lecture.values()) != 0:
            grade_list = []
            for v in self.grade_lecture.values():
                grade_list.extend(v)
            mean_grade = sum(grade_list) / len(grade_list)
            return mean_grade
        return 'Error'

    def __str__(self):
        res = (f'Имя: {self.name.capitalize()} \n'
               f'Фамилия: {self.surname.capitalize()} \n'
               f'Средняя оценка за лекции: {self.__average_grade():.1f}')
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.__average_grade() < other.__average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        """ Add grade to dict grades in class Student """
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error'

    def __str__(self):
        res = (f'Имя: {self.name.capitalize()} \n'
               f'Фамилия: {self.surname.capitalize()}')
        return res


# Exercise 4:
# Used name like: first_... and second_... Student, Lecture, Reviewer:

first_student = Student('Roy', 'Man', 'gender')
first_student.courses_in_progress += ['Git']
first_student.courses_in_progress += ['Python']
second_student = Student('Anna', 'Key', 'your_gender')
second_student.courses_in_progress += ['Git']
second_student.courses_in_progress += ['Python']

first_reviewer = Reviewer('Andrey', 'Day')
first_reviewer.courses_attached += ['Git']
first_reviewer.courses_attached += ['Python']
second_reviewer = Reviewer('Mike', 'New')
second_reviewer.courses_attached += ['Git']
second_reviewer.courses_attached += ['Python']

first_lecturer = Lecturer('Boris', 'Ray')
first_lecturer.courses_attached += ['Git']
first_lecturer.courses_attached += ['Python']
second_lecturer = Lecturer('Egor', 'Fedorov')
second_lecturer.courses_attached += ['Git']
second_lecturer.courses_attached += ['Python']

first_student.finished_courses += ['Введение в программирование']

# Rate for Student:
first_student.rate_hw(first_lecturer, 'Git', 9)
first_student.rate_hw(first_lecturer, 'Python', 4)
first_student.rate_hw(second_lecturer, 'Git', 9)
first_student.rate_hw(second_lecturer, 'Python', 9)

# Rate for Reviewer:
first_reviewer.rate_hw(first_student, 'Python', 11)
first_reviewer.rate_hw(first_student, 'Python', 4)
first_reviewer.rate_hw(first_student, 'Git', 1)
first_reviewer.rate_hw(second_student, 'Python', 2)
first_reviewer.rate_hw(second_student, 'Git', 6)

# For test __str__:
print(first_student)
# print(first_lecturer)
# print(first_reviewer)

# For test __lt__:
# print(first_student < second_student)
# print(first_lecturer < second_lecturer)

people_studying = [first_student, second_student]
lecturer_learner = [first_lecturer, second_lecturer]


def average_grade_course(student_list, course_name):
    """ Average grades for all students in selected course """
    if len(student_list) != 0:
        grades_list = []
        for student in student_list:
            for course, grade in student.grades.items():
                if course == course_name:
                    grades_list.extend(grade)
        if len(grades_list) != 0:
            mean_grades = sum(grades_list) / len(grades_list)
            return round(mean_grades, 1)
    return 'Error'


def average_grade_lecturer(lecturer_list, course_name=None):
    """ Average grades for all lecturer in selected courses, default for all courses """
    if len(lecturer_list) != 0:
        grades_list = []
        for lecturer in lecturer_list:
            for course, grade in lecturer.grade_lecture.items():
                if course == course_name or course_name is None:
                    grades_list.extend(grade)
        if len(grades_list) != 0:
            mean_grades = sum(grades_list) / len(grades_list)
            return round(mean_grades, 1)
    return 'Error'


# print(average_grade_course(people_studying, 'Python'))
# print(average_grade_lecturer(lecturer_learner, 'Python'))
