# -*- coding: utf-8 -*-
"""python_day_8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ow7AymcZMMDRrM2T-al5G-yTDdf0t_I-
"""

num = 1234
rev_num = 0

while num>0:
  temp = num % 10 #last digit
  rev_num = rev_num * 10 + temp
  num = num//10  #delete last digit

  print(rev_num)

"""# conditional statement

# if - else

# il - elif

#pass,continue,break
"""

num = int(input("Enter the number:-"))

if num>0:
  print("the number is positive")
else:
  print("the number is negative")

#even-odd

num = 9

if num % 2==0:
  print("even number")

else:
    print("odd number")

num = float(input("Enter the number:-"))

#voting eligibility

age = 16

if age>=18:
  print("you are eligible to vote")
else:
  print("you are not eligible to vote.")

marks = 49

if marks >= 90:
  print("gradeA")
elif marks >=80:
  print('gradeB')
elif marks>=70:
  print("gradeC")
elif marks>=50:
  print("gradeD")
else:
  print("Fail")

