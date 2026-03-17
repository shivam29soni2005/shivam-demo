
# relation between salary and experience and predict salary with the expreince basis 

# gether the data from csv file


import pandas as pd 

df=pd.read_csv("test.csv")

print(df)

print(df.info())

# data visualizing in bar chart

import matplotlib.pyplot as plt

x=df["experience"]
y=df["salary_usd"]

plt.bar(x,y)

plt.show()

# machine learning model for prediction 


from sklearn.linear_model import LinearRegression


x=df[["experience"]]
y=df["salary_usd"]

model=LinearRegression()

model.fit(x,y)

exprience=float(input("enter your experience:"))

prediction=model.predict([[exprience]])

print(prediction)


