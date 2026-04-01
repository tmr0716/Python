print('----------------------------------- Classroom Day 9 -----------------------------------')
import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset from Day 8
df = pd.read_csv("students.csv")
df.head()

                                            # Basic structure example
plt.figure(figsize=(6, 4))
plt.plot([1, 2, 3], [10, 20, 15])
plt.title("Basic Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()
plt.figure(figsize=(7, 4))
plt.hist(df["marks"], bins=10, color="skyblue", edgecolor="black")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()
                                            #Calculate average marks per city
city_avg = df.groupby("city")["marks"].mean().sort_values()

plt.figure(figsize=(7, 4))
plt.bar(city_avg.index, city_avg.values, color="lightgreen")
plt.title("Average Marks by City")
plt.xlabel("City")
plt.ylabel("Average Marks")
plt.show()

                                            # Sort by joining date
df_sorted = df.sort_values("joined_at")

plt.figure(figsize=(8, 4))
plt.plot(df_sorted["joined_at"], df_sorted["marks"], marker="o", color="purple")
plt.title("Marks Trend by Joining Date")
plt.xlabel("Joining Date")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

plt.figure(figsize=(6, 4))
plt.scatter(df["age"], df["marks"], color="orange", edgecolor="black")
plt.title("Age vs Marks")
plt.xlabel("Age")
plt.ylabel("Marks")
plt.show()

                                            # Define colors for each city
colors = {
    "MUMBAI": "blue",
    "DELHI": "red",
    "PUNE": "orange",
    "BENGALURU": "green",
    "UNKNOWN": "gray"
}

plt.figure(figsize=(7, 5))
for city, color in colors.items():
    subset = df[df["city"] == city]
    plt.scatter(subset["age"], subset["marks"], label=city, color=color, s=100)

plt.title("Age vs Marks (City-Wise)")
plt.xlabel("Age")
plt.ylabel("Marks")
plt.legend()
plt.show()

                                            # Boxplot
plt.figure(figsize=(6, 4))
plt.boxplot(df["marks"], vert=False)
plt.title("Marks Outlier Detection")
plt.xlabel("Marks")
plt.show()

                                            # Pie Chart
plt.figure(figsize=(6, 6))
counts = df["city"].value_counts()
plt.pie(counts, labels=counts.index, autopct="%1.1f%%", startangle=140)
plt.title("City Representation")
plt.show()

                                            # Subplots
# Create a 1x2 grid of subplots
fig, ax = plt.subplots(1, 2, figsize=(10, 4))

# Left plot: Histogram
ax[0].hist(df["marks"], bins=10, color="skyblue", edgecolor="black")
ax[0].set_title("Marks Distribution")
ax[0].set_xlabel("Marks")
ax[0].set_ylabel("Frequency")

# Right plot: Scatter
ax[1].scatter(df["age"], df["marks"], color="orange")
ax[1].set_title("Age vs Marks")
ax[1].set_xlabel("Age")
ax[1].set_ylabel("Marks")

plt.tight_layout()
plt.show()

                                            # Annotations
plt.figure(figsize=(7, 4))
plt.plot(df_sorted["joined_at"], df_sorted["marks"], marker="o")
plt.title("Marks Over Time")

                                            # Highlight the highest mark
top = df_sorted.loc[df_sorted["marks"].idxmax()]
plt.annotate(f"Topper: {top['name']}",
             xy=(top["joined_at"], top["marks"]),
             xytext=(top["joined_at"], top["marks"] + 5),
             arrowprops=dict(facecolor='red', arrowstyle="->"))

plt.show()

print(df)