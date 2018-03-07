#grading.py
grade=input("What is your grade?")
grade= int(grade)
if grade % 10 > 6:
    plus_minus= '+'
elif grade % 10 < 4:
    plus_minus= '-'
else:
    plus_minus=''
if grade >= 90 and grade <= 100:
    print("A"+ plus_minus)
elif grade > 80 and grade <= 89:
  print("B" + plus_minus)
elif grade >= 70 and grade <= 79:
  print("C" + plus_minus)
elif grade >= 60 and grade <= 69:
  print("D" + plus_minus)
else:
    print("F")
