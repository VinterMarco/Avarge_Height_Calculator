# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# DONT USE sum() or len()

# Write your code below this row 👇

# My way

sum = 0
counter = 0
for height in student_heights:
    sum += height  # asa adunam toate elementele din lista iterata
    counter += 1  # asa aflam cate elemente avem in lista iterata
avarage = sum / counter
print(f"The avarage height of the students is {avarage}")

# angela's way

# total_heigts = 0
# for height in student_heights:
#      total_heigts += height
#
# number_of_students = 0
# for student in student_heights:
#     number_of_students = number_of_students + 1
#
# avarage = total_heigts / number_of_students
# print(avarage)
