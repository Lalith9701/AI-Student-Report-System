import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv(r"C:\Users\lalit\OneDrive\Desktop\student report system\student_report_system\student_data.csv")
    

# ------------------ BASIC REPORTS ------------------
print("📊 Student Report Summary")
print("="*40)

# Subject-wise average
print("\nSubject-wise Average Marks:")
print(df[['Maths','Science','English']].mean())

# Highest & Lowest scorer in each subject
print("\nHighest Scorers:")
print(df[['Maths','Science','English']].idxmax())

print("\nLowest Scorers:")
print(df[['Maths','Science','English']].idxmin())

# Overall performance of each student
df['Total'] = df[['Maths','Science','English']].sum(axis=1)
df['Average'] = df['Total'] / 3

print("\nOverall Student Performance:")
print(df[['Name','Total','Average','Attendance']])

# ------------------ VISUALIZATIONS ------------------

# Bar chart: subject-wise averages
df[['Maths','Science','English']].mean().plot(kind='bar', color=['blue','green','orange'])
plt.title("Subject-wise Average Marks")
plt.ylabel("Average Marks")
plt.show()

# Pie chart: Attendance
plt.pie(df['Attendance'], labels=df['Name'], autopct='%1.1f%%')
plt.title("Attendance Distribution")
plt.show()

# Line graph: Individual student performance
for subject in ['Maths','Science','English']:
    plt.plot(df['Name'], df[subject], marker='o', label=subject)

plt.title("Student Performance by Subject")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.legend()
plt.show()

