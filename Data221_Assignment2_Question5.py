import pandas as pd

data = pd.read_csv("student.csv")

data["grade_band"] = ""

# Low: grade ≤ 9
data.loc[data["grade"] <= 9, "grade_band"] = "Low"

# Medium: grade between 10 and 14
data.loc[(data["grade"] >= 10) & (data["grade"] <= 14), "grade_band"] = "Medium"

# High: grade ≥ 15
data.loc[data["grade"] >= 15, "grade_band"] = "High"


summary_data = []

for band in ["Low", "Medium", "High"]:
    group = data.loc[data["grade_band"] == band]

    numberOfStudents = len(group)
    averageAbsences = group["absences"].mean()
    percentageInternetAccess = group["internet"].mean() * 100

    summary_data.append([band, numberOfStudents, averageAbsences, percentageInternetAccess])

#Convert summary list to DataFrame
summary = pd.DataFrame(summary_data, columns=[
    "grade_band",
    "numberOfStudents",
    "averageAbsences",
    "percentageInternetAccess"
])

#  Save to CSV
summary.to_csv("student_bands.csv", index=False)

# Print result
print(summary)
