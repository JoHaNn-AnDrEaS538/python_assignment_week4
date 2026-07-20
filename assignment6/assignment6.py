grade = [55, 70, 65, 40, 90, 85, 50, 77]
grade1 = list(filter(lambda x: x>=60, grade))
bonus = list(map(lambda x: x+(0.05*x),grade1))
print("Grades passed with bonus=",bonus)