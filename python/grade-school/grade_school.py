class School(object):
    def __init__(self):
        self.students = list()

    def add_student(self, name, grade):
        # Add the student information as a list in list of students
        self.students.append([name, grade])
        return self.students.sort()

    def roster(self):
        # Used list comprehension in list comprehension because wasn't applying the sort
        return [name[0] for name in \
                sorted([student for student in self.students], key=lambda x: (x[1], x[0]))]

    def grade(self, grade_number):
        # Sorted Method sort alphabetical by name. List Comprehension extract the students name
        return sorted([student[0] for student in self.students if student[1] == grade_number])

# First tried with dictionary
# class School(object):
#     # Method used to multiple sort
#     from operator import attrgetter
#
#     def __init__(self):
#         self.students = dict()
#
#     def add_student(self, name, grade):
#         self.students.update({name: grade})
#         return sorted(self.students.keys())
#
#     def roster(self):
#         # Falta terminar de ordenar. Precisa ser primeiro pelo grade, depois pelo nome do aluno
#         from operator import itemgetter
#         # return sorted(self.students.keys(), key=lambda key: (key[1], key[0]))
#         return sorted(self.students.keys(), key=itemgetter(1, 0))
#
#     def grade(self, grade_number):
#         student_by_grade = [key for (key, value) in self.students.items() if value == grade_number]
#         return sorted(student_by_grade)
