import pandas as pd 
from simple_linearreg import *

df = pd.read_csv("Salary_dataset.csv")

year = df["YearsExperience"].to_numpy()
sala = df["Salary"].to_numpy()

b0,b1 = simple_linregressor(year,sala)

exp = float(input("Enter Experience : "))
salr = b0 + b1*exp

print("Expected Salary : ",salr)