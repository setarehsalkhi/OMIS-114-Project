import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("StudentPerformanceFactors.csv")
df2 = df.drop(columns = ['Access_to_Resources', 'Previous_Scores', 'Internet_Access', 'Teacher_Quality', 'Parental_Education_Level', 'Tutoring_Sessions', 'School_Type', 'Physical_Activity', 'Learning_Disabilities', 'Distance_from_Home'], inplace = False)

def f(x):
    if (x == "Low") | (x == "Negative"):
        return 0
    elif (x == 'Medium') | (x == "Neutral"):
        return 0.5
    elif (x == 'High') | (x == "Positive"):
        return 1
df2['Motivation_Level'] = df2['Motivation_Level'].apply(f)
df2['Family_Income'] = df2['Family_Income'].apply(f)
df2['Peer_Influence'] = df2['Peer_Influence'].apply(f)

def g(x):
    if x == "Yes":
        return 1.0
    elif x == "No":
        return 0.0
df2['Extracurricular_Activities'] = df2['Extracurricular_Activities'].apply(g)