import pandas as pd


def setRiskLevel (violentCrimesPerPop):
    if violentCrimesPerPop >= 0.50:
        return "High-Crime"
    else:
        return "LowCrime"

dataFrame = pd.read_csv("crime.csv", delimiter=",")

dataFrame["risk"] = dataFrame["ViolentCrimesPerPop"].apply(setRiskLevel)

high_crime = dataFrame.loc[dataFrame["risk"] == "High-Crime"]
low_crime = dataFrame.loc[dataFrame["risk"] == "LowCrime"]

high_average_unemployment = high_crime["PctUnemployed"].mean()
low_average_unemployment = low_crime["PctUnemployed"].mean()


print("Average unemployment rate for High-Crime areas:", high_average_unemployment)
print("Average unemployment rate for LowCrime areas:", low_average_unemployment)
