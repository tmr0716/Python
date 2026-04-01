print('----------------------------------- Classroom Day 8 -----------------------------------')
import pandas as pd
# from datetime import date

# rows = [
#     {"name":"Sahil","city":"MUMBAI","age":19,"marks":87,"joined_at":"2024-07-12"},
#     {"name":"Isha","city":"DELHI","age":20,"marks":93,"joined_at":"2024-07-15"},
#     {"name":"Aarav","city":"PUNE","age":18,"marks":76,"joined_at":"2024-07-18"},
#     {"name":"Riya","city":"MUMBAI","age":None,"marks":64,"joined_at":"2024-08-01"},
#     {"name":"Kabir","city":"DELHI","age":21,"marks":None,"joined_at":"2024-08-03"},
#     {"name":"Anaya","city":"BENGALURU","age":20,"marks":55,"joined_at":"2024-08-05"},
#     {"name":"Vihaan","city":"DELHI","age":22,"marks":39,"joined_at":"2024-08-07"},
#     {"name":"Aanya","city":"","age":19,"marks":72,"joined_at":"2024-08-09"},
#     {"name":"Ansh","city":" MUMBAI ","age":20,"marks":101,"joined_at":"2024-08-12"},
#     {"name":"Ira","city":"PUNE","age":18,"marks":-5,"joined_at":"2024-08-14"},
# ]

# pd.DataFrame(rows).to_csv("students.csv", index=False)
# print("students.csv written with", len(rows), "rows")

df = pd.read_csv('students.csv')
# a = df.head(3)
# b = df.info()
# c = df.describe()
# print(b)
# print(c)
# print(df)

# a = df.isna()
# b = df.fillna(a.sum(), inplace=True)
# c = df["marks"].fillna(df['marks'].median)
# print(a)
# print(b)
# print(c)
