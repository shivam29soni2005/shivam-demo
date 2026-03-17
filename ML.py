import pandas as pd

data={'name':["shivam","kanu","ram","lucky","ansh","gagan"],

     'marks':[89,98,99,100,79,80],  
        
      'attendence':[85,78,90,95,68,70]
}


df=pd.DataFrame(data)

print(df)

df.to_csv("data.csv",index=False)


import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data=pd.read_csv("data.csv")
print(data)


plt.plot(df["marks"],df["attendence"])

plt.title('relation between marks and attendence')

plt.xlabel("marks")
plt.ylabel("attendence")

plt.show()

model=LinearRegression()

x=df[["attendence"]]
y=df["marks"]


model.fit(x,y)

attendence=float(input("enter the your attendence"))

# new_data = pd.DataFrame([[80]], columns=["attendence"])

output=model.predict([[attendence]])

print(output)

if attendence<=50:
    print("yee kam marks h")
elif attendence>=50:
    print("yee ache marks h")    












