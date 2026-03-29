print('----------------------------------- Classroom Day 5 -----------------------------------')
# print('----------------------------------- FOR LOOP -----------------------------------')
# n=1
# for n in range(1,301):
#     print(n,"Toshan")
# print('----------------------------------- WHILE LOOP -----------------------------------')
# c = 7
# guess = 0
# while guess != c:
#     guess = int(input("Guess a number: "))
# print("Congratulations! You've guessed the number.")
# print('----------------------------------- BREAK/CONTINUE/PASS -----------------------------------')
# for i in range(5):
#     if i == 2: continue
#     if i == 4: break
#     print(i)
# print('----------------------------------- HANDS ON MINI-PROJECT -----------------------------------')
# c = 7
# guess = 0
# while guess != c:
#     guess = int(input("Guess a number: "))
#     if guess < c:
#         print("Wrong!Try Again!")
#     elif guess > c:
#         print("Wrong!Try Again!")
#     else:
#         print("Congratulations! You've guessed the number.")
print('----------------------------- Homework -----------------------------')
print(" ----- Even numbers from 1 to 50 ----- ")
for i in range(1, 51):
    if i % 2 == 0:
        print(i)
print(" ----- Counting Vowels ----- ")
text = input("Enter a String: ")
vowels = "AEIOUaeiou"
c = 0
for str in text:
    if str in vowels:
        c += 1
print("Number of vowels:", c)
print(" ----- Multiplication Table ----- ")
table = int(input("A number for multiplication table: "))
for m in range(1, 11):
    print(table, "x", m, "=", table * m)
# Mini Project: Simple Calculator 
# Use functions