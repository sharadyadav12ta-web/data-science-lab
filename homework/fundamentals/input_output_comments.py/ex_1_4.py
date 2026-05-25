name = input("enter your name")
math_marks = int(input("enter your marks"))
science_marks = int(input("enter your marks"))
english_marks = int(input("enter your marks"))
percentage = (math_marks+ science_marks+ english_marks ) / 300*100
print(f"{name} scored {percentage}% in exam.")