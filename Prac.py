import pandas as pd
import matplotlib.pyplot as plt
data = [
    ["name", "age", "city", "marks", "joined_at"],
    ["Rahul Sharma", "22", "Mumbai", "85", "2024-01-15"],
    ["Priya Patel", "21", "delhi",   "92", "2024-01-18"],
    ["Amit Kumar", "", "PUNE",     "78", "2024-01-20"],
    ["Sneha Singh", "23", "bangalore", "105", "2024-01-22"],
    ["Vikram Rao", "20", "Mumbai", "67", "2024-02-01"],
    ["Ananya Desai", "24", "", "88", "2024-02-05"],
    ["Rohan Gupta", "19", "DELHI", "45", "2024-02-10"],
    ["Meera Joshi", "22", "pune", "91", "2024-02-15"],
    ["Karan Mehta", "25", "Bangalore", "72", "2024-02-20"],
    ["Ishita Verma", "", "mumbai", "-5", "2024-02-25"],
    ["Arjun Nair", "21", "Delhi", "58", "2024-03-01"],
    ["Kavya Reddy", "23", "  ", "83", "2024-03-05"],
    ["Aditya Iyer", "20", "MUMBAI", "110", "2024-03-10"],
    ["Riya Shah", "22", "bangalore", "94", "2024-03-15"],
    ["Sanjay Kumar", "24", "Pune", "36", "2024-03-20"],
    ["Neha Chopra", "", "Delhi", "89", "2024-03-25"],
    ["Manish Tiwari", "21", "mumbai", "73", "2024-04-01"],
    ["Pooja Srinivas", "23", "BANGALORE", "61", "2024-04-05"],
    ["Varun Malhotra", "22", "", "79", "2024-04-10"],
    ["Divya Krishnan", "20", "pune", "97", "2024-04-15"],
    ["Akash Pandey", "25", "Mumbai", "42", "2024-04-20"],
    ["Ritika Bose", "", "delhi", "86", "2024-04-25"],
    ["Harsh Agarwal", "21", "Bangalore", "55", "2024-05-01"],
    ["Swati Kulkarni", "24", "PUNE", "68", "2024-05-05"],
    ["Nikhil Saxena", "23", "  mumbai  ", "90", "2024-05-10"],
    ["Anjali Rao", "22", "DELHI", "38", "2024-05-15"],
    ["Rajesh Kumar", "20", "bangalore", "-10", "2024-05-20"],
    ["Shreya Banerjee", "", "Mumbai", "82", "2024-05-25"],
    ["Gaurav Singh", "25", "pune", "76", "2024-06-01"],
    ["Tanvi Sharma", "21", "", "95", "2024-06-05"],
    ["Aryan Jain", "23", "Delhi", "120", "2024-06-10"],
    ["Nisha Menon", "22", "mumbai", "64", "2024-06-15"],
    ["Deepak Yadav", "24", "BANGALORE", "87", "2024-06-20"],
    ["Aarti Deshmukh", "", "pune", "71", "2024-06-25"],
    ["Vishal Gupta", "20", "Mumbai", "49", "2024-07-01"],
    ["Simran Kaur", "21", "delhi", "93", "2024-07-05"],
    ["Mayank Joshi", "23", "  ", "81", "2024-07-10"],
    ["Pallavi Rajan", "22", "bangalore", "56", "2024-07-15"],
    ["Rohit Verma", "25", "PUNE", "99", "2024-07-20"],
    ["Kritika Singh", "", "Mumbai", "74", "2024-07-25"]
]
pd.DataFrame(data).to_csv("practice.csv", index=False)
df = pd.read_csv("practice.csv")
df.head()
print(df)

plt.figure(figsize=(7, 5))
plt.plot([1, 2, 3], [10, 20, 15])
plt.title("Basic Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df["marks"], bins=10, color="skyblue", edgecolor="black")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].scatter(df["name"], df["marks"], color="blue")
ax[0].set_title("Name vs Marks")
ax[0].set_xlabel("Name")
ax[0].set_ylabel("Marks")
plt.tight_layout()
plt.show()

ax[1].scatter(df["name"], df["marks"], color="orange")
ax[1].set_title("Name vs Marks")
ax[1].set_xlabel("Age")
ax[1].set_ylabel("Marks")
plt.tight_layout()
plt.show()
