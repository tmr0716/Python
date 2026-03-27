# Create mini calculator
print("Enter operator: +,-,/,*,//,**,%")
op = input()
print("Enter first number:")
num1 = input()
print("Enter second number:")
num2 = input()
if op == '+':
    ans = float(num1) + float(num2)
if op == '-':
    ans = float(num1) - float(num2)
if op == '*':
    ans = float(num1) * float(num2)
if op == '/':
    ans = float(num1) / float(num2)
if op == '//':
    ans = float(num1) // float(num2)
if op == '**':
    ans = float(num1) ** float(num2)
if op == '%':
    ans = float(num1) % float(num2)
else:
    ans = "Invalid Operator"
print("The answer is: {}".format(ans))
# Use 5 string Methods
print("Enter a string:")
str_input = input()
upper_ans = str_input.upper()
lower_ans = str_input.lower()
title_ans = str_input.title()
replace_ans = str_input.replace('Nilay', 'University')
print(str_input.swapcase())
print("Uppercase: {}".format(upper_ans))
print("Lowercase: {}".format(lower_ans))
print("Title: {}".format(title_ans))
print("Replaced: {}".format(replace_ans))
# Try input() + format()
