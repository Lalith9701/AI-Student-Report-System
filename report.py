
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_data.csv")
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_data.csv", on_bad_lines='skip')

df.columns = df.columns.str.strip()

if "Name" in df.columns:
    df["Name"] = df["Name"].astype(str).str.strip()

print("📊 Student Report Summary")
print("=" * 40)

print("\nSubject-wise Average Marks:")
print(df[['Maths', 'Science', 'English']].mean())

print("\nHighest Scorers (Row Index):")
print(df[['Maths', 'Science', 'English']].idxmax())

print("\nLowest Scorers (Row Index):")
print(df[['Maths', 'Science', 'English']].idxmin())

df['Total'] = df[['Maths', 'Science', 'English']].sum(axis=1)
df['Average'] = df['Total'] / 3

print("\nOverall Student Performance:")
print(df[['Name', 'Total', 'Average', 'Attendance']])

df[['Maths', 'Science', 'English']].mean().plot(
    kind='bar', color=['blue', 'green', 'orange']
)
plt.title("Subject-wise Average Marks")
plt.ylabel("Average Marks")
plt.show()

plt.pie(df['Attendance'], labels=df['Name'], autopct='%1.1f%%')
plt.title("Attendance Distribution")
plt.show()

for subject in ['Maths', 'Science', 'English']:
    plt.plot(df['Name'], df[subject], marker='o', label=subject)

plt.title("Student Performance by Subject")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.legend()
plt.show()

    
print("📊 Student Report Summary")
print("="*40)

print("\nSubject-wise Average Marks:")
print(df[['Maths','Science','English']].mean())

print("\nHighest Scorers:")
print(df[['Maths','Science','English']].idxmax())

print("\nLowest Scorers:")
print(df[['Maths','Science','English']].idxmin())

df['Total'] = df[['Maths','Science','English']].sum(axis=1)
df['Average'] = df['Total'] / 3

print("\nOverall Student Performance:")
print(df[['Name','Total','Average','Attendance']])

df[['Maths','Science','English']].mean().plot(kind='bar', color=['blue','green','orange'])
plt.title("Subject-wise Average Marks")
plt.ylabel("Average Marks")
plt.show()

plt.pie(df['Attendance'], labels=df['Name'], autopct='%1.1f%%')
plt.title("Attendance Distribution")
plt.show()

for subject in ['Maths','Science','English']:
    plt.plot(df['Name'], df[subject], marker='o', label=subject)

plt.title("Student Performance by Subject")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.legend()
plt.show()



