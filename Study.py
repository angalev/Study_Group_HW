class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def calc_grade(self, grades):
        mean = lambda x: sum(x) / len(x)
        mean_dic = {k: mean(v) for k, v in self.grades.items() if len(v) > 0}
        if any([v for v in self.grades.values()]) == True:
            return round(mean([mean_dic[c] for c in mean_dic]), 2)
        else:
            return "Нет оценок"

    def __str__(self):
        return (f"Имя: {self.name}\n"
               f"Фамилия: {self.surname}\n"
               f"Средняя оценка за домашние задания: {self.calc_grade(self.grades)}\n"
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
               f"Завершенные курсы: {', '.join(self.finished_courses)}")

# comparison functions for student's average grade
    def __eq__(self, other_grades):
        return self.calc_grade(self.grades) == other_grades.calc_grade(other_grades.grades)

    def __lt__(self, other_grades):
        return self.calc_grade(self.grades) < other_grades.calc_grade(other_grades.grades)

    def __le__(self, other_grades):
        return self.calc_grade(self.grades) <= other_grades.calc_grade(other_grades.grades)

    def __gt__(self, other_grades):
        return self.calc_grade(self.grades) > other_grades.calc_grade(other_grades.grades)

    def __ge__(self, other_grades):
        return self.calc_grade(self.grades) >= other_grades.calc_grade(other_grades.grades)

# rate lecturer
    def rate_lc(self, lecturer, course, rate):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress or course in self.finished_courses:
            if course in lecturer.rate:
                lecturer.rate[course] += [rate]
            else:
                lecturer.rate[course] = [rate]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Lecturer's name: {self.name}, surname {self.surname}."


# Subclasses
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rate = {}

# lecturer rating calculator
    def calc_rate(self, rate):
        mean = lambda x: sum(x) / len(x)
        mean_dic = {k: mean(v) for k, v in self.rate.items() if len(v) > 0}
        if any([v for v in self.rate.values()]) == True:
            return round(mean([mean_dic[c] for c in mean_dic]), 2)
        else:
            return "Нет оценок"

    def __str__(self):
       return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.calc_rate(self.rate)}"

# comparison functions for lecturer's average rate
    def __eq__(self, other_rate):
        return self.calc_rate(self.rate) == other_rate.calc_rate(other_rate.rate)

    def __lt__(self, other_rate):
        return self.calc_rate(self.rate) < other_rate.calc_rate(other_rate.rate)

    def __le__(self, other_rate):
        return self.calc_rate(self.rate) <= other_rate.calc_rate(other_rate.rate)

    def __gt__(self, other_rate):
        return self.calc_rate(self.rate) > other_rate.calc_rate(other_rate.rate)

    def __ge__(self, other_rate):
        return self.calc_rate(self.rate) >= other_rate.calc_rate(other_rate.rate)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} "

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('!!!Ошибка, несоответствие курсов!!!')

# functions
def course_grade(student_list, course_name):
    grades = 0
    counter = 0
    for student in student_list:
        if course_name in student.grades:
            grades += sum(student.grades[course_name])
            counter += len(student.grades[course_name])
        if counter > 0:
            return grades / counter
        else:
            return 0

def course_rating(lecturers_list, course_name):
    rating = 0
    counter = 0
    for lecturer in lecturers_list:
        if course_name in lecturer.rate:
            rating += sum(lecturer.rate[course_name])
            counter += len(lecturer.rate[course_name])
        if counter > 0:
            return rating / counter
        else:
            return 0

## testing
# add objects
student1 = Student('Raisa', 'Ivanovna', 'non-binar')
student2 = Student('Владимир', 'Владимиров', 'М')
student1.finished_courses += ['Marketing', 'Industrial design']
student2.finished_courses += ['Marketing', 'Industrial design', 'Programming']
student1.courses_in_progress += ['Python']
student2.courses_in_progress += ['Дизайн']
lecturer1 = Lecturer('Konstantin', 'Petrov')
lecturer2 = Lecturer('Гвидо', 'ван Россум')
reviewer1 = Reviewer('Кот', 'Матроскин')
reviewer2 = Reviewer('Mikhail', 'Angalev')
reviewer1.courses_attached += ['C#', 'Python']
reviewer2.courses_attached += ['C#', 'Python', 'Дизайн']

# test methods
lecturer1.rate['Python'] = [3, 5, 10]
lecturer2.rate['Design'] = [10, 9, 9]
reviewer1.rate_hw(student1, 'Python', 1)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer2.rate_hw(student2, 'Дизайн', 1)
reviewer2.rate_hw(student2, 'Python', 10)

#output
print(student1, '\n', student2, sep='\n')
print()
print(lecturer1, '\n', lecturer2, sep='')
print()
print(reviewer1,  '\n', reviewer2, sep='')
print()
print(lecturer1 < lecturer2)
print(course_grade([student1, student2], 'Python'))
print(course_rating([lecturer1, lecturer2], 'Python'))
