from roster import student_roster
import classroom_organizer
import itertools


student_roster_iterator = iter(student_roster)
# print(next(student_roster_iterator))
# print(next(student_roster_iterator))
# print(next(student_roster_iterator))
# print(next(student_roster_iterator))

students = classroom_organizer.ClassroomOrganizer()

for student in student_roster_iterator:
    print(student)

pairs = students.student_combinations()
for pair in pairs:
    print(pair)

best_future = itertools.chain(students.get_students_with_subject("Math"), students.get_students_with_subject("Science"))
best_groups = itertools.combinations(best_future, 4)
for group in best_groups:
    print(group)
