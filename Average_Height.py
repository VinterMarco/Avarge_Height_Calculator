student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
sum = 0
counter = 0
for height in student_heights:
    sum += height  
    counter += 1  
avarage = sum / counter
print(f"The avarage height of the students is {avarage}")
