import pandas as pd

studentDataFrame = pd.read_csv("student.csv", delimiter=",")
filteredStudents = studentDataFrame[(studentDataFrame['studytime']>=3) & (studentDataFrame['internet']==1) & (studentDataFrame['absences']<=5)]


filteredStudents.to_csv("high_engagement.csv", index=False)
print("number of students saved: ", len(filteredStudents))
print("their average grade: ", filteredStudents["grade"].mean())