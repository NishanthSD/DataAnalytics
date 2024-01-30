from sklearn.linear_model import LogisticRegression
import numpy as np
from math import *

xValues = [0.25+i*0.25 for i in range(20)]
yValues = [0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1]
xValues = [[i] for i in xValues]

model = LogisticRegression(solver='lbfgs')
model.fit(xValues, yValues)

b0 = model.intercept_[0]
b1 = model.coef_[0][0]

hrs = float(input("Enter the hours of study : "))
pred = 1/(1+pow(e,-(b0 + b1*hrs)))

print("Percentage to pass: ",round(pred*100,2),"%")