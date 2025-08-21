import pandas as pd

data = []

while True:
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    maths = int(input("Enter Maths marks: "))
    science = int(input("Enter Science marks: "))
    english = int(input("Enter English marks: "))
    attendance = int(input("Enter attendance percentage: "))

    data.append([name, roll, maths, science, english, attendance])

    cont = input("Do you want to add another student? (yes/no): ")
    if cont.lower() != 'y':
        break

df = pd.DataFrame(data, columns=['Name', 'Roll No', 'Maths', 'Science', 'English', 'Attendance'])
print("\nFinal Report:")
print(df)

df.to_csv("student_data.csv", index=False)
print("\nData saved to student_data.csv")
